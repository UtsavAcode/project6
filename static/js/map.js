var map = L.map('map').setView([0, 0], 13);
var marker;

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to update user location on the map and store latitude and longitude
function updateUserLocation(latitude, longitude) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker([latitude, longitude]).addTo(map);

    // Store latitude and longitude in hidden input fields
    document.getElementById("latitude").value = latitude;
    document.getElementById("longitude").value = longitude;
}

// Function to handle map click events
function onMapClick(e) {
    var latitude = e.latlng.lat;
    var longitude = e.latlng.lng;
    updateUserLocation(latitude, longitude);
}

// Add click event listener to the map
map.on('click', onMapClick);
