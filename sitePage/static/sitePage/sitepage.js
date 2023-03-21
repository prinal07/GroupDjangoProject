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
if (url != "localhost:8000") {
    x = url.replace('-', ' ');
    newUrl = "EcoExeter - ".concat(capitalizeFirstLetter(url))
    document.title = newUrl
} else{
    newUrl2 = "EcoExeter - ".concat("Home")
    document.title = newUrl2
}