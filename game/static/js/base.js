
/**
 * Toggle the side navbar
 */
function sidebarToggle() {
    var sidebar = document.querySelector("#sidebar");
    var container = document.querySelector(".sidenav-container");
    if (sidebar.classList.contains('active-nav')) {
        sidebar.classList.remove('active-nav');
        container.classList.remove('active-cont');
    } else {
        sidebar.classList.add('active-nav');
        container.classList.add('active-cont');
    }

}

// Updating page title depending on active page
let activeHref = window.location.href;
url = activeHref.split('/').filter(Boolean).pop();

/**
 * Capitalizes the first letter of a string
 * @param {str} string 
 * @returns 
*/
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
if (url != "game") {
    x = url.replace('-', ' ');
    newUrl = "Eco-Detective - ".concat(capitalizeFirstLetter(url))
    document.title = newUrl
} else {
    newUrl2 = "Eco-Detective - ".concat("Home")
    document.title = newUrl2
}
