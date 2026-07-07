"""
SudsFlow Analytics — Car Wash Sales Dashboard
Web version of the original Samsung Innovative Campus CLI project.
Same business logic (discount month, surcharge month, coupon customers,
customer ranking, monthly sales, time-of-day split) — reimplemented on
top of the CSV export instead of a live MySQL connection, so it can run
anywhere without a database.
"""

import os
from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "car_wash_sales_data.csv")

# ---------------------------------------------------------------------------
# Data loading — loaded once at startup and kept in memory (small dataset)
# ---------------------------------------------------------------------------

def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    # Make sure derived columns exist even if the source CSV lacks them
    if "hour" not in df.columns:
        df["hour"] = df["date"].dt.hour
    if "month" not in df.columns:
        df["month"] = df["date"].dt.month
    if "day_part" not in df.columns:
        df["day_part"] = pd.cut(
            df["hour"],
            bins=[0, 6, 12, 18, 24],
            labels=["Night", "Morning", "Afternoon", "Evening"],
            right=False,
        )
    return df


df = load_data()

MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


# ---------------------------------------------------------------------------
# Routes — page
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------------------------------------
# Routes — API (each mirrors a function from the original CRUD module)
# ---------------------------------------------------------------------------

@app.route("/api/summary")
def api_summary():
    total_revenue = int(df["amount"].sum())
    total_washes = int(len(df))
    avg_ticket = round(total_revenue / total_washes, 2) if total_washes else 0
    total_customers = int(df["cust_id"].nunique())
    return jsonify({
        "total_revenue": total_revenue,
        "total_washes": total_washes,
        "avg_ticket": avg_ticket,
        "total_customers": total_customers,
    })


@app.route("/api/monthly")
def api_monthly():
    monthly = df.groupby("month")["amount"].sum().reindex(range(1, 13), fill_value=0)
    return jsonify({
        "labels": [MONTH_NAMES[m - 1] for m in monthly.index],
        "values": [int(v) for v in monthly.values],
    })


@app.route("/api/discount-surcharge-month")
def api_discount_surcharge():
    monthly = df.groupby("month")["amount"].sum()
    discount_month = int(monthly.idxmin())
    surcharge_month = int(monthly.idxmax())
    return jsonify({
        "discount_month": {"month": MONTH_NAMES[discount_month - 1], "amount": int(monthly.min())},
        "surcharge_month": {"month": MONTH_NAMES[surcharge_month - 1], "amount": int(monthly.max())},
    })


@app.route("/api/day-part")
def api_day_part():
    grouped = df.groupby("day_part", observed=False)["amount"].sum()
    order = ["Morning", "Afternoon", "Evening", "Night"]
    grouped = grouped.reindex(order, fill_value=0)
    return jsonify({
        "labels": list(grouped.index),
        "values": [int(v) for v in grouped.values],
    })


@app.route("/api/top-customers")
def api_top_customers():
    grouped = df.groupby("cust_id").agg(
        last_visit=("date", "max"),
        total_spent=("amount", "sum"),
    ).sort_values("total_spent", ascending=False).head(5)
    return jsonify([
        {
            "cust_id": int(idx),
            "last_visit": row["last_visit"].strftime("%Y-%m-%d"),
            "total_spent": int(row["total_spent"]),
        }
        for idx, row in grouped.iterrows()
    ])


@app.route("/api/ranking")
def api_ranking():
    grouped = df.groupby("cust_id")["amount"].sum().sort_values(ascending=False).head(5)
    return jsonify([
        {"rank": i + 1, "cust_id": int(idx), "total_spent": int(val)}
        for i, (idx, val) in enumerate(grouped.items())
    ])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
