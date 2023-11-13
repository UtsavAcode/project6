document.addEventListener("DOMContentLoaded", function () {
    var canvas = document.getElementById('registrationChart');
    var registrationCount = canvas.getAttribute('data-registration-count');

    var ctx = canvas.getContext('2d');

    var chart = new Chart(ctx, {
        type: 'line',  // Change the chart type to 'line'
        data: {
            labels: ['Registrations This Month'],
            datasets: [{
                label: 'Number of Registrations',
                data: [registrationCount],
                borderColor: 'rgba(75, 192, 192, 1)',  // Line color
                fill: false,  // Do not fill the area under the line
                borderWidth: 2  // Line width
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
