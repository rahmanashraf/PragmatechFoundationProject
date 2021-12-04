var x = document.getElementById("myAudio");

function playAudio() {
    x.play();
}

function pauseAudio() {
    x.pause();
}

// function basla() {
//     var x = document.getElementById("ButtonBasla");
//     if (x.style.display === "none") {
//         x.style.display = "block";
//     } else {
//         x.style.transform = "translate(0,-350px)"
//         x.innerHTML = "Uğurlar!";
//         x.style.transition = "1s ease";
//         setTimeout('window.open(\'http://127.0.0.1:5500/game\')', 5000)
//     }
// }