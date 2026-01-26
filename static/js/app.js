fetch("/chart-data")
    .then(response => response.json())
    .then(data => {
        if (!data || Object.keys(data).length === 0) {
            return
        }

        if (data.time_distribution) {
            new Chart(document.getElementById("timeChart"), {
                type: "bar",
                data: {
                    labels: Object.keys(data.time_distribution),
                    datasets: [{ data: Object.values(data.time_distribution) }]
                }
            })
        }

        if (data.task_distribution) {
            new Chart(document.getElementById("taskChart"), {
                type: "pie",
                data: {
                    labels: Object.keys(data.task_distribution),
                    datasets: [{ data: Object.values(data.task_distribution) }]
                }
            })
        }

        if (data.energy_trend && data.energy_trend.length > 0) {
            new Chart(document.getElementById("energyChart"), {
                type: "line",
                data: {
                    labels: data.energy_trend.map((_, i) => i + 1),
                    datasets: [{ data: data.energy_trend }]
                }
            })
        }
    })