const colors = ["#FF6384", "#36A2EB", "#FFCE56", "#FF638499", "#36A2EB99", "#FFCE5699"];
const today = new Date().getTime()

const last_seven_days = [
  today - 6 * 24 * 60 * 60 * 1000,
  today - 5 * 24 * 60 * 60 * 1000,
  today - 4 * 24 * 60 * 60 * 1000,
  today - 3 * 24 * 60 * 60 * 1000,
  today - 2 * 24 * 60 * 60 * 1000,
  today - 24 * 60 * 60 * 1000,
  today,
]

function addZero(i) {
  if (i < 10) {
    i = "0" + i
  }
  return i
}

for (let i = 0; i < last_seven_days.length; i++) {
  date = new Date(last_seven_days[i])
  last_seven_days[i] = addZero(date.getDate())  + "." + addZero((date.getMonth()+1));
}

const income_data = [];
const expense_data = [];
const balance_data = [];

for (let i = 0; i < last_seven_days.length; i++) {
  const transaction = finance_data[i]

  if (`${transaction.type}` === "income") {
    income_data.push(transaction.amount)
    expense_data.push(0)

    if (i === 0) {
      balance_data.push(transaction.amount)
    } else {
      balance_data.push(balance_data[i - 1] + transaction.amount)
    }
  } else {
    income_data.push(0)
    expense_data.push(transaction.amount)

    if (i === 0) {
      balance_data.push(-transaction.amount)
    } else {
      balance_data.push(balance_data[i - 1] - transaction.amount)
    }
  }
}

/* large line chart */
const chLine = document.getElementById("chLine");
const chartData = {
  labels: last_seven_days,
  datasets: [
    {
      data: income_data,
      backgroundColor: 'transparent',
      borderColor: colors[0],
      borderWidth: 4,
      pointBackgroundColor: colors[0]
    },
    {
      data: expense_data,
      backgroundColor: 'transparent',
      borderColor: colors[1],
      borderWidth: 4,
      pointBackgroundColor: colors[1]
    },
    {
      data: balance_data,
      backgroundColor: colors[5],
      borderColor: colors[2],
      borderWidth: 4,
      pointBackgroundColor: colors[2]
    }
  ]
};
if (chLine) {
  new Chart(chLine, {
    type: 'line',
    data: chartData,
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      },
      responsive: true
    }
  });
}
