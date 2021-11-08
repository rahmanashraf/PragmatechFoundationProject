let color = ["#fff100", "#2eb82e", "#ff0000", "#0000ff", "#993366", "#a3a375"]
let x = 0
document.querySelector("button").addEventListener("click",
    function() {
        x = 1 < color.length ? ++x : 0
        document.querySelector("body").style.background = color[x]
        document.getElementById("span").innerHTML = color[x]
    })