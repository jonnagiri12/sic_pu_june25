const fmtCurrency = (n) => '₹' + Number(n).toLocaleString('en-IN');
const fmtNumber = (n) => Number(n).toLocaleString('en-IN');

async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to fetch ${url}`);
  return res.json();
}

async function loadSummary() {
  const data = await fetchJSON('/api/summary');
  document.getElementById('kpi-revenue').textContent = fmtCurrency(data.total_revenue);
  document.getElementById('kpi-washes').textContent = fmtNumber(data.total_washes);
  document.getElementById('kpi-avg').textContent = fmtCurrency(data.avg_ticket);
  document.getElementById('kpi-customers').textContent = fmtNumber(data.total_customers);
}

async function loadMonthly() {
  const data = await fetchJSON('/api/monthly');
  const ctx = document.getElementById('monthlyChart');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.labels,
      datasets: [{
        data: data.values,
        backgroundColor: '#1E9CB0',
        borderRadius: 6,
        maxBarThickness: 34,
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: {
        y: { ticks: { callback: (v) => '₹' + v.toLocaleString('en-IN') }, grid: { color: '#eef3f3' } },
        x: { grid: { display: false } }
      }
    }
  });
}

async function loadDiscountSurcharge() {
  const data = await fetchJSON('/api/discount-surcharge-month');
  document.getElementById('discount-month').textContent = data.discount_month.month;
  document.getElementById('discount-amount').textContent = fmtCurrency(data.discount_month.amount);
  document.getElementById('surcharge-month').textContent = data.surcharge_month.month;
  document.getElementById('surcharge-amount').textContent = fmtCurrency(data.surcharge_month.amount);
}

async function loadDayPart() {
  const data = await fetchJSON('/api/day-part');
  const colors = ['#F2C14E', '#1E9CB0', '#E4572E', '#0E3A45'];
  const ctx = document.getElementById('dayPartChart');
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        data: data.values,
        backgroundColor: colors,
        borderWidth: 0,
      }]
    },
    options: {
      responsive: true,
      cutout: '62%',
      plugins: { legend: { display: false } }
    }
  });

  const total = data.values.reduce((a, b) => a + b, 0);
  const legend = document.getElementById('daypart-legend');
  legend.innerHTML = data.labels.map((label, i) => {
    const pct = total ? ((data.values[i] / total) * 100).toFixed(1) : 0;
    return `<div class="legend-row">
      <span class="legend-dot" style="background:${colors[i]}"></span>
      <span class="legend-label">${label}</span>
      <span class="legend-value">${pct}% · ${fmtCurrency(data.values[i])}</span>
    </div>`;
  }).join('');
}

async function loadTopCustomers() {
  const data = await fetchJSON('/api/top-customers');
  const tbody = document.querySelector('#coupon-table tbody');
  tbody.innerHTML = data.map(row => `
    <tr>
      <td>#${row.cust_id}</td>
      <td>${row.last_visit}</td>
      <td>${fmtCurrency(row.total_spent)}</td>
    </tr>
  `).join('');
}

async function loadRanking() {
  const data = await fetchJSON('/api/ranking');
  const tbody = document.querySelector('#ranking-table tbody');
  const medals = ['🥇', '🥈', '🥉'];
  tbody.innerHTML = data.map(row => `
    <tr>
      <td>${medals[row.rank - 1] || row.rank}</td>
      <td>#${row.cust_id}</td>
      <td>${fmtCurrency(row.total_spent)}</td>
    </tr>
  `).join('');
}

(async function init() {
  try {
    await Promise.all([
      loadSummary(),
      loadMonthly(),
      loadDiscountSurcharge(),
      loadDayPart(),
      loadTopCustomers(),
      loadRanking(),
    ]);
  } catch (err) {
    console.error(err);
  }
})();
