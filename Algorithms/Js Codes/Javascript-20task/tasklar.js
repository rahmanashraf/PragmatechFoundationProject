/* TASK-1: 2 ededi tipində məlumatı parametr olaraq qəbul edib ededlərin hasilini return edən funksiya yazın

function hasil(x, y) {
    return (x * y)
}

hasilim = hasil(5, 7)
document.write(hasilim) */




/* TASK2. 1 eded parametr qəbul edib daxil edilən dəyərin 1 artığını return elətdirən funksiya yazın
NOT-Problemi solve eledim amma duz elemis olduguma emin deyilem hardasa sehvim var
let x = 1

function artim(x) {

    return x++

}
aybrats = x++
    document.write(x) */


/*TASK3.il dəyəri daxil edildiyi zaman onun necə ay və necə gün olduğunu
return edən funksiya yazın
NOT - PRoblemi hell ettim amma nese netice gec berpa olunur alert edende bele olmurdu amma documentwritedan sonra bele oldu neyse allah bereket versin
*/
function ilhesabi(ay = 12, gun = 365) {
    let netice = prompt(" x qeder il nece aydir ve neche gundur?")
    let cavab1 = ay * netice
    let cavab2 = gun * netice
    document.write("verdiyiniz sayda il " + cavab1 + "  aydir " + cavab2 + "  gundur")


}
ilhesabi()



/* TASK4.Parametr olaraq array qəbul edən və daxil edilən arrayın ilk elementini return edən funksiya yazın
NOT.cavabimin yolxanilmasin istirem cunki mence elebilki hardasa sehv elirem return tam catmib mene qebul elirem


function kitab() {
    let kitab = ["salam", "qaqas", "atas", "balas"]
    console.log(kitab[0])
    return [0]
}
kitab()*/




/* TASK5.Daxil edilən 5 parametri array formasında return edən funksiya yazın.
NOT- yene cixardim ortaya what a hell return o yene qimiwir
function kitab() {
    let kitab = ["salam", "qaqas", "atas", "balas", "atasim"]
    kitab = [0, 1, 2, 3, 4]
    console.log(kitab)
    return
}
kitab() */



/*TASK 6 alindira bilmedim nese

let yas = [15, 16, 17, 18, 19, 20, 21, 22, 25]
yas.forEach(yas * 2)
console.log(yas) */




// let samir = 'Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
// console.log(samir.length)  TASK7.8 deqiq bilmedim hansini elemis oldum neyse saol

// netice = samir.split(",")
// console.log(netice)     Task12 de bele getdi


// netice = samir.split(" ")    TASK9 CONGRATULATIONNN QAQASHHHH
// console.log(netice)


// netice = samir.split(" ", 10)
// console.log(netice)                        TASK11 CONGRATULATIONNNNN QAQAS

// kabab = samir.search(ortaya)
// console.log(kabab)