alert("Toplama proqramina xos geldiniz");
alert("siz burada ededlerin toplamini vermelisiniz");
let x = prompt("zehmet olmasa lazim olan ededi giriniz");
let toplama = 0
while (Number(x) != 0) {
    toplama = toplama + Number(x)
    x = prompt(" Toplamag ucun eded girin qaqas....")
}
alert("toplam" + toplama)