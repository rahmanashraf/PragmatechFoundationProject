const text = document.getElementById('text')
const prog = 'MAL HULYA'
let idx = 1;
setInterval(writetext, 500)

function writetext() {
    text.innerText = prog.slice(0, idx)
    idx++
    if (idx > prog.length) {
        idx = 1
    }
}