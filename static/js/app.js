fetch("/chart-data")
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById("timeChart").getContext("2d")
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: Object.keys(data),
                datasets: [{
                    data: Object.values(data)
                }]
            }
        })
    })