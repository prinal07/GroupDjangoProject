/**
 * Capitalizes the first letter of a string
 * @param {str} string 
 * @returns 
*/
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// Updating page title depending on active page
let activeHref = window.location.href;
url = activeHref.split('/').filter(Boolean).pop();

// update the URL to display the specific page
if (url != "eco-mystery.herokuapp.com") {
    x = url.replace('-', ' ');
    newUrl = "EcoMystery - ".concat(capitalizeFirstLetter(url))
    document.title = newUrl
} if (url != "eco-mystery.herokuapp.com/") {
    newUrl2 = "EcoMystery - ".concat("Home")
    document.title = newUrl2
} else {
    newUrl2 = "EcoMystery - ".concat("Home")
    document.title = newUrl2
}