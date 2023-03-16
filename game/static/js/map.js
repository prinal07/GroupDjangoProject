/**
 * Gets the current geolocation of the user and sends it to the locationParser function.
 * If geolocation is not supported by the browser, displays an error message.
 */
 function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("location-button").innerHTML = "Geolocation is not supported by this browser.";
        console.log("Geolocation is not supported by this browser.");
    }
}

/**
 * Callback function for getCurrentPosition. Extracts the latitude and longitude from the position object,
 * and passes them to the locationParser function. Also logs the current location to the console.
 * 
 * @param {Object} position - The position object returned by getCurrentPosition.
 */
function showPosition(position) {
    let lat = position.coords.latitude;
    let lng = position.coords.longitude;
    locationParserToReceiver(lat, lng);
    console.log("Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude);
}

/**
 * Sends a POST request to the specified URL with the provided latitude and longitude data.
 * 
 * @param {number} latitude - The latitude of the user's current location.
 * @param {number} longitude - The longitude of the user's current location.
 */
function locationParserToReceiver(latitude, longitude){
    $.ajax({
        type: "POST",
        url: "/game/Receiver/",
        data: {
            'latitude': latitude,
            'longitude': longitude,
            'csrfmiddlewaretoken': '{{ csrf_token }}' 
        },
        success: function(data) {
            console.log("Data sent successfully");
        },
        error: function(xhr, status, error) {
            console.log("Error sending data: " + error);
        }
    });
}
function getFinalLocation(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showFinalPosition);
    } else {
        document.getElementById("final-location-button").innerHTML = "Geolocation is not supported by this browser.";
        console.log("Geolocation is not supported by this browser.");
    }
}

function showFinalPosition(position) {
    let lat = position.coords.latitude;
    let lng = position.coords.longitude;
    locationParserToget_Directions(lat, lng);
    console.log("Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude);
}
function locationParserToget_Directions(latitude, longitude){

    $.ajax({
        type: "POST",
        url: "/game/get_Directions/",
        data: {
            'latitude': latitude,
            'longitude': longitude,
            'csrfmiddlewaretoken': '{{ csrf_token }}' 
        },
        success: function(data) {
            console.log("Data sent successfully");
        },
        error: function(xhr, status, error) {
            console.log("Error sending data: " + error);
        }
    });
}