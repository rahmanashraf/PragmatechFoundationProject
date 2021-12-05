var birSual = document.getElementById("sual1");
var ikiSual = document.getElementById("sual2");
var ucSual = document.getElementById("sual3");
var dordSual = document.getElementById("sual4");
var besSual = document.getElementById("sual5");
var birCavab = document.getElementById("duzgun1");
var ikiCavab = document.getElementById("duzgun2");
var ucCavab = document.getElementById("duzgun3");
var dordCavab = document.getElementById("duzgun4");
var besCavab = document.getElementById("duzgun5");
var suallar = document.getElementById('suallar');
var bye = document.getElementById('bye');
var final = document.getElementById('final');
var intro = document.getElementById('intro');
var main = document.getElementById('main');
var phone = document.getElementById('phone');
var win = document.getElementById('win');
var wrong = document.getElementById('wrong');
var dostazenget = document.getElementById("dostazengele")
var ellielliye = document.getElementById("ellilik")
var userss = document.getElementById("users")
var letsgo = document.getElementById("lets")
var help = document.getElementById("fastes")
var giris = document.getElementById("myAudio")


function basladig() {
    giris.play()
    userss.remove()

}


function dostazeng() {
    phone.play()
    dostazenget.remove()
}

function elli() {
    if (birSual.style.display = "block") {
        document.getElementById("sehv1-1").style.background = "white"
        document.getElementById("sehv1-2").style.background = "white"
        ellielliye.remove()
    } else
        alert("blaaa")
}

function audit() {
    help.play()
}


function sehv1() {
    document.getElementById("sehv1-1").style.backgroundColor = "red";
    document.getElementById("sehv1-2").style.backgroundColor = "red";
    document.getElementById("sehv1-3").style.backgroundColor = "red";
    wrong.play()
    window.open("/game")

}

function sehv2() {
    document.getElementById("sehv2-1").style.backgroundColor = "red";
    document.getElementById("sehv2-2").style.backgroundColor = "red";
    document.getElementById("sehv2-3").style.backgroundColor = "red";
    wrong.play()
    window.open("/game")

}

function sehv3() {
    document.getElementById("sehv3-1").style.backgroundColor = "red";
    document.getElementById("sehv3-2").style.backgroundColor = "red";
    document.getElementById("sehv3-3").style.backgroundColor = "red";
    window.open("/game")
    wrong.play()
}

function sehv4() {
    document.getElementById("sehv4-1").style.backgroundColor = "red";
    document.getElementById("sehv4-2").style.backgroundColor = "red";
    document.getElementById("sehv4-3").style.backgroundColor = "red";
    wrong.play()
    window.open("/game")

}

function sehv5() {
    document.getElementById("sehv5-1").style.backgroundColor = "red";
    document.getElementById("sehv5-2").style.backgroundColor = "red";
    document.getElementById("sehv5-3").style.backgroundColor = "red";
    wrong.play()
    window.open("/game")

}


function duzgun1() {
    if (birCavab.style.background = "#4d2065") {
        birCavab.style.background = "green"
        birCavab.innerHTML = "Cavab doğrudur-next(2click) "
        win.play()
        document.getElementById("app").innerHTML = "SIZIN XALINIZ-1"
    } else {
        alert("hey")
    }
}

function duzgun2() {
    if (ikiCavab.style.background = "#4d2065") {
        ikiCavab.style.background = "green"
        ikiCavab.innerHTML = "Cavab doğrudur-next(2click) "
        win.play()
        document.getElementById("app").innerHTML = "SIZIN XALINIZ-2"
    } else {
        alert("hey")
    }
}

function duzgun3() {
    if (ucCavab.style.background = "#4d2065") {
        ucCavab.style.background = "green"
        ucCavab.innerHTML = "Cavab doğrudur-next(2click) "
        win.play()
        document.getElementById("app").innerHTML = "SIZIN XALINIZ-3"
    } else {
        alert("hey")
    }
}


function duzgun4() {
    if (dordCavab.style.background = "#4d2065") {
        dordCavab.style.background = "green"
        dordCavab.innerHTML = "Cavab doğrudur-next(2click) "
        win.play()
        document.getElementById("app").innerHTML = "SIZIN XALINIZ-4"
    } else {
        alert("hey")
    }
}


function duzgun5() {
    if (besCavab.style.background = "#4d2065") {
        besCavab.style.background = "green"
        besCavab.innerHTML = "Cavab doğrudur-next(2click) "
        win.play()
        document.getElementById("app").innerHTML = "SIZ QALIBSINIZ"
    } else {
        alert("hey")
    }
}


// loopa salmaliam bu gediw yaxshi gedirw deil
// 
// 




function duzgunn1() {
    if (ikiSual.style.display = "none") {
        ikiSual.style.display = "block"
        ucSual.style.display = "none"
        dordSual.style.display = "none"
        besSual.style.display = "none"
        birSual.style.display = "none"
        letsgo.play()

    } else {
        alert("sehv cavabdi")

    }
}

function duzgunn2() {
    if (ucSual.style.display = "none") {
        ucSual.style.display = "block"
        ikiSual.style.display = "none"
        dordSual.style.display = "none"
        besSual.style.display = "none"
        birSual.style.display = "none"
        letsgo.play()

    } else {
        alert("sehv cavabdi")

    }
}


function duzgunn3() {
    if (dordSual.style.display = "none") {
        dordSual.style.display = "block"
        ucSual.style.display = "none"
        ikiSual.style.display = "none"
        besSual.style.display = "none"
        birSual.style.display = "none"
        letsgo.play()

    } else {
        alert("sehv cavabdi")

    }
}

function duzgunn4() {
    if (besSual.style.display = "none") {
        besSual.style.display = "block"
        ikiSual.style.display = "none"
        dordSual.style.display = "none"
        ucSual.style.display = "none"
        birSual.style.display = "none"
        letsgo.play()

    } else {
        alert("sehv cavabdi")

    }
}

function duzgunn5() {


}