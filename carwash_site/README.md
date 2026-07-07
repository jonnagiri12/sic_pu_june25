# SudsFlow Analytics — Car Wash Sales Dashboard

Web version of the original **Samsung Innovative Campus** internship project
(CLI + MySQL + matplotlib) — same analytics, now a live, interactive website.

## What it does

Reads `data/car_wash_sales_data.csv` and serves:

| Feature | Original CLI function | Web equivalent |
|---|---|---|
| Discount month (lowest revenue) | `discount_month()` | `/api/discount-surcharge-month` |
| Surcharge month (highest revenue) | `surcharge_month()` | `/api/discount-surcharge-month` |
| Coupon-worthy customers | `coupon_customers()` | `/api/top-customers` |
| Customer ranking | `customers_ranking()` | `/api/ranking` |
| Monthly sales | `monthly_sales_of_year()` | `/api/monthly` |
| Sales by time of day (pie chart) | `display_ofsales_using_piechart()` | `/api/day-part` (doughnut chart) |

No database needed — the CSV is loaded into memory with pandas at startup.

## Project structure

```
carwash_site/
├── app.py                  # Flask app + API routes
├── data/
│   └── car_wash_sales_data.csv
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── Procfile                # for deployment
```

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Use YOUR own data

Replace `data/car_wash_sales_data.csv` with your real file — just keep the
same columns: `date, cust_id, service_id, amount, hour, day_part, month`.
Restart the app and the dashboard updates automatically.

## Deploy for free — Render.com

1. Push this folder to a **GitHub repo** (create one on github.com, then:)
   ```bash
   git init
   git add .
   git commit -m "SudsFlow Analytics dashboard"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

2. Go to **https://render.com** → sign up (free, no card needed for this tier)

3. Click **New +** → **Web Service** → connect your GitHub repo

4. Render should auto-detect Python. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

5. Click **Create Web Service** — Render builds and deploys automatically.
   You'll get a live URL like `https://sudsflow-analytics.onrender.com`

Note: on Render's free tier, the app "sleeps" after 15 min of inactivity and
takes ~30s to wake up on the next visit — fine for a portfolio/demo project.

## Credit

Original analytics logic and CLI app built during Samsung Innovative Campus
internship. This is a web front-end and deployment wrapper around that work.
