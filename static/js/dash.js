fetch('/search/?search=' + query)
    .then(response => response.json())
    .then(data => {
        if ('message' in data) {
            // Display an alert indicating no results found
            alert(data.message);
        } else {
            // Handle the search results as usual
            console.log(data); // Display the search results in the console
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

// JavaScript (dash.js)

// Add a click event listener to the "Close" link
