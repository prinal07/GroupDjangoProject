/**
 * Toggle the side navbar
 */
function sidebarToggle() {
    var sidebar = document.querySelector("#sidebar");
    var container = document.querySelector(".sidenav-container");
    if (sidebar.classList.contains('active-sidebar')) {
        sidebar.classList.remove('active-sidebar');
        container.classList.remove('active-cont');
    } else {
        sidebar.classList.add('active-sidebar');
        container.classList.add('active-cont');
    }

}

// Updating page title depending on active page
url = window.location.href.split('/').filter(Boolean).pop();

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
    newUrl = "EcoMystery - ".concat(capitalizeFirstLetter(url))
    document.title = newUrl
} else {
    newUrl2 = "EcoMystery - ".concat("Home")
    document.title = newUrl2
}
