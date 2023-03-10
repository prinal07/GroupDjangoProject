mapboxgl.accessToken = 'pk.eyJ1Ijoic2MxMTMxIiwiYSI6ImNsZXBqYTNoNjBjcGIzdG81djdwazN4ZnoifQ.aUnfUV2U5KPxxgPni-Ma1Q';
        const map = new mapboxgl.Map({
            container: 'map',
// Choose from Mapbox's core styles, or make your own style with Mapbox Studio
            style: 'mapbox://styles/mapbox/streets-v12',
            center: [-3.5356537, 50.7368255],
            zoom: 16
        });

        console.log(bin_info);

        var marker = null;
        var popup = null;

        popup = new mapboxgl.Popup({offset: 25}).setText("PIN INFO 1");

        marker = new mapboxgl.Marker().setLngLat([-3.537214,50.738053]).setPopup(popup).addTo(map);

        popup = new mapboxgl.Popup({offset: 25}).setText("PIN INFO 2");
        marker = new mapboxgl.Marker().setLngLat([-3.531119,50.738331]).setPopup(popup).addTo(map);

        popup = new mapboxgl.Popup({offset: 25}).setText("PIN INFO 3");
        marker = new mapboxgl.Marker().setLngLat([-3.536073,50.736282]).setPopup(popup).addTo(map);

        popup = new mapboxgl.Popup({offset: 25}).setText("PIN INFO 4");
        marker = new mapboxgl.Marker().setLngLat([-3.535000,50.739100]).setPopup(popup).addTo(map);

        for (var i = 0; i < bin_info.length; i++) {
            let lat = parseFloat(bin_info[i][0]);
            let lon = parseFloat(bin_info[i][1]);

            popup = new mapboxgl.Popup({offset: 25}).setText(bin_info[i][2]);

            marker = new mapboxgl.Marker()
                .setLngLat([lon, lat])
                .setPopup(popup)
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
// These coordinates outline Maine.
                        'coordinates': [
                            [
                                [-3.54012113,50.7393587],
                                [-3.5382954,50.7381304],
                                [-3.5372081,50.7394105 ],
                               
                            ]
                        ]
                    }
                }
            });
            map.addSource('exeter', {
                'type': 'geojson',
                'data': {
                    'type':'Feature',
                    'geometry': {
                        'type': 'Polygon',
                        'coordinates': [
                            [
                                [-3.5341631,50.7418840],
                                [-3.5335790,50.7403587],
                                [-3.5312515,50.7410841],
                                [-3.5324632, 50.7422746]
                            ]
                        ]
                    }
                }
            });
            map.addSource('park3', {
                'type': 'geojson',
                'data': {
                    'type':'Feature',
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
                                [-3.5319415,50.7341617],
                                [-3.5314349, 50.7340736],
                                [-3.5324445,50.7332753],
                                [-3.5319436,50.7330960 ]
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

        map.on('load', () => {

        })
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
    locationParser(lat, lng);
    console.log("Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude);
}

/**
 * Sends a POST request to the specified URL with the provided latitude and longitude data.
 * 
 * @param {number} latitude - The latitude of the user's current location.
 * @param {number} longitude - The longitude of the user's current location.
 */
function locationParser(latitude, longitude){
    $.ajax({
        type: "POST",
        url: "/game/your_view/",
        data: {
            'latitude': latitude,
            'longitude': longitude,
            'csrfmiddlewaretoken': '{{ csrf_token }}' // add this if using Django's CSRF protection
        },
        success: function(data) {
            console.log("Data sent successfully");
        },
        error: function(xhr, status, error) {
            console.log("Error sending data: " + error);
        }
    });
}

       
