const text = document.getElementById('text')
const prog = 'WE LOVE PROGRAMMING'
let idx = 1;
setInterval(writetext, 300)

function writetext() {
    text.innerText = prog.slice(0, idx)
    idx++
    if (idx > prog.length) {
        idx = 1
    }
}