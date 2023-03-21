levelDiv = document.getElementById("current-level").innerHTML
level = parseInt(levelDiv.split('Level: ').pop());

if (level >= 3) {
    // badge that displays if level 3 or higher
    document.getElementById("eco2").style.display = "block"
} 
if (level >= 5) {
    // badge that displays if level 5 or higher
    document.getElementById("eco3").style.display = "block"
}