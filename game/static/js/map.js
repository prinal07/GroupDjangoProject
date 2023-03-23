mapboxgl.accessToken = 'pk.eyJ1Ijoic2MxMTMxIiwiYSI6ImNsZXBqYTNoNjBjcGIzdG81djdwazN4ZnoifQ.aUnfUV2U5KPxxgPni-Ma1Q';

const geojson = {
    'type': 'FeatureCollection',
    'features': [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [-3.537214, 50.738053]
            },
            'properties': {
                'title': 'Bin 1',
                'description': 'Recycle now!'
            }
        },
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [-3.531119, 50.738331]
            },
            'properties': {
                'title': 'Bin 2',
                'description': 'Recycle now!'
            }
        },
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [-3.536073, 50.736282]
            },
            'properties': {
                'title': 'Bin 3',
                'description': 'Recycle now!'
            }
        },
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [-3.535000, 50.739100]
            },
            'properties': {
                'title': 'Bin 4',
                'description': 'Recycle now!'
            }
        }
    ]
};
const map = new mapboxgl.Map({
    container: 'map',
// Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [-3.5352823, 50.7371627],
    zoom: 16
});


for (const feature of geojson.features) {
    // create a HTML element for each feature
    const el = document.createElement('div');
    el.className = 'marker';

    // make a marker for each feature and add it to the map
    new mapboxgl.Marker(el)
        .setLngLat(feature.geometry.coordinates)
        .setPopup(
            new mapboxgl.Popup({offset: 25}) // add popups
                .setHTML(
                    `<h3>${feature.properties.title}</h3>
    <p>${feature.properties.description}</p>`
                )
        )
        .addTo(map);
}


map.on('load', () => {
// Add a data source containing GeoJSON data.
    map.addSource('maine', {
        'type': 'geojson',
        'data': {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',

                'coordinates': [
                    [
                        [-3.54012113, 50.7393587],
                        [-3.5382954, 50.7381304],
                        [-3.5372081, 50.7394105],

                    ]
                ]
            }
        }
    });

    points = [
        [-3.5341631, 50.7418840],
        [-3.5335790, 50.7403587],
        [-3.5312515, 50.7410841],
        [-3.5324632, 50.7422746]
    ]

    map.addSource('exeter', {
        'type': 'geojson',
        'data': {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [

                    points

                ]
            }
        }
    });
    map.addSource('park3', {
        'type': 'geojson',
        'data': {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [-3.5293083,50.7364445 ],
                        [-3.5291410,50.7358839],
                        [-3.5298109,50.7360017],
                        [-3.5299208, 50.7363348]
                    ]
                ]
            }
        }
    });
    map.addSource('park4', {
        'type': 'geojson',
        'data': {
            'type':'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [-3.5374679,50.7287101],
                        [ -3.5364497,50.7280259],
                        [-3.5353282,50.7280361],
                        [-3.5356284,50.7289626 ]
                    ]
                ]
            }
        }
    });
    map.addSource('park5', {
        'type': 'geojson',
        'data': {
            'type':'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [-3.5319415, 50.7341617],
                        [-3.5314349, 50.7340736],
                        [-3.5324445, 50.7332753],
                        [-3.5319436, 50.7330960]
                    ]
                ]
            }
        }
    });


    map.addSource('park6', {
        'type': 'geojson',
        'data': {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [

                        [-3.532288932448523, 50.7359873845501],
                        [-3.5334667225815792, 50.73694531506939],
                        [-3.5340531117119554, 50.736653497251154],


                    ]
                ]
            }
        }
    });
    map.addLayer({
        'id': 'park5',
        'type': 'fill',
        'source': 'park5', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });

    map.addLayer({
        'id': 'park6',
        'type': 'fill',
        'source': 'park6', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
    // Add a new layer to visualize the polygon.
    map.addLayer({
        'id': 'maine',
        'type': 'fill',
        'source': 'maine', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
    map.addLayer({
        'id': 'exeter',
        'type': 'fill',
        'source': 'exeter', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
    map.addLayer({
        'id': 'park3',
        'type': 'fill',
        'source': 'park3', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
    map.addLayer({
        'id': 'park4',
        'type': 'fill',
        'source': 'park4', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
})

var geolocate = new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
// When active the map will receive updates to the device's location as it changes.
    trackUserLocation: true,
// Draw an arrow next to the location dot to indicate which direction the device is heading.
    showUserHeading: true
})
// Add geolocate control to the map.
map.addControl(
    geolocate
);

geolocate.on('geolocate', function (e) {
    var lon = e.coords.longitude;
    var lat = e.coords.latitude
    var currentPosition = [lon, lat];
    console.log(currentPosition);

    $.ajax({
        type: "POST",
        url: ".",
        data: {
            'lat': lat,
            'lon': lon,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function (data) {
            if (data["within_area"]) {
                console.log("user in area");
                window.alert(data["within_area"]);
            } else if (data["too_soon"]) {
                console.log("user in area too soon");
                window.alert(data["too_soon"]);
            } else {
                console.log("User not within area at this time");
            }
        },
        error: function (xhr, status, error) {
            console.log("Error sending data: " + error);
        }
    });
});

// add markers to map
map.on('load', function () {
    // Add a new GeoJSON source with the geojson object
    map.addSource('markers', {
        type: 'geojson',
        data: geojson
    });

    // Add markers to the map using the GeoJSON source
    map.addLayer({
        id: 'markers',
        type: 'symbol',
        source: 'markers',
        layout: {
            'icon-image': 'bin.png', // Use the 'bin' image for markers
            'icon-size': 0.5,
            'text-field': '{title}',
            'text-offset': [0, 1],
            'text-anchor': 'top'
        }
    });
});


map.on('mousemove', (e) => {
    document.getElementById('info').innerHTML =
// `e.point` is the x, y coordinates of the `mousemove` event
// relative to the top-left corner of the map.
        JSON.stringify(e.point) +
        '<br />' +
        // `e.lngLat` is the longitude, latitude geographical position of the event.
        JSON.stringify(e.lngLat.wrap());
});



// /**
//  * Gets the current geolocation of the user and sends it to the locationParser function.
//  * If geolocation is not supported by the browser, displays an error message.
//  */
// function getLocation() {
// if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showPosition);
// } else {
//     document.getElementById("location-button").innerHTML = "Geolocation is not supported by this browser.";
//     console.log("Geolocation is not supported by this browser.");
// }
// }

// /** Callback function for getCurrentPosition. Extracts the latitude and longitude from the position object,
// * and passes them to the locationParser function. Also logs the current location to the console.
// * 
// * @param {Object} position - The position object returned by getCurrentPosition.
// */
// function showPosition(position) {
// let lat = position.coords.latitude;
// let lng = position.coords.longitude;
// locationParserToReceiver(lat, lng);
// console.log("Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude);
// }

// /** 
//  * Sends a POST request to the specified URL with the provided latitude and longitude data.
//  * @param {number} latitude - The latitude of the user's current location.
//  * @param {number} longitude - The longitude of the user's current location.
// */
// function locationParserToReceiver(latitude, longitude){
// $.ajax({
//     type: "POST",
//     url: "./Receiver",
//     data: {
//         'latitude': latitude,
//         'longitude': longitude,
//         'csrfmiddlewaretoken': '{{ csrf_token }}' 
//     },
//     success: function(data) {
//         console.log("Data sent successfully");
//     },
//     error: function(xhr, status, error) {
//         console.log("Error sending data: " + error);
//     }
// });
// }
// /**
//  * Requests the user's geolocation and calls showFinalPosition with the position data.
//  * If geolocation is not supported by the browser, displays an error message.
// */
// function getFinalLocation() {
// if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showFinalPosition);
// } else {
//     document.getElementById("final-location-button").innerHTML = "Geolocation is not supported by this browser.";
//     console.log("Geolocation is not supported by this browser.");
// }
// } 

// /** Parses the user's position data to retrieve latitude and longitude,
// * and calls locationParserToget_Directions to retrieve directions based on the user's location.
// * @param {Object} position - the user's position data, obtained from navigator.geolocation.getCurrentPosition
// */
// function showFinalPosition(position) {
//     let lat = position.coords.latitude;
//     let lng = position.coords.longitude;
//     locationParserToget_Directions(lat, lng);
//     console.log("Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude);
// }

// /** Sends an AJAX request to retrieve directions based on the user's location.
// * @param {number} latitude - the user's latitude
// * @param {number} longitude - the user's longitude
// */
// function locationParserToget_Directions(latitude, longitude) {
// $.ajax({
//     type: "POST",
//     url: "./get_Directions",
//     data: {
//         'latitude': latitude,
//         'longitude': longitude,
//         'csrfmiddlewaretoken': '{{ csrf_token }}' // included to prevent CSRF attacks
//     },
//     success: function(data) {
//         console.log("Data sent successfully");
//     },
//     error: function(xhr, status, error) {
//         console.log("Error sending data: " + error);
//     }
// });
// }