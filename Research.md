### Task kitab Class python
1. bir dene class acirig BookInfo adinda
2. def init (self,yazar,buraxilis ili,nesriyatevi,kitabinmovzusu)
3. sonra self.yazar self.buraxilisili ve sair yazirig bu funksia ready
4. birdenede def acirig bookinformation(self) altina nese metod lazimdisa eger o tipde self.ve sair yazirig hazir qoyurug

1. class acirig Booksale adinda
2. def init (self, alisqiymeti,satisqiymeti, satis tarixi,qalanxeyir,endirim)
3. burada yene self.alisqiymetisatisqiymeti yazirig altalta
4. birdenede def acirig booksale(self) altina nese metod lazimdisa eger o tipde self.ve sair yazirig hazir qoyurug

1. class acirig Staffinfo adinda
2. def init (self, ad,soyad,vezife,maas,isebaslamatarixi)
3. burada yene self. ad soyad vezife yazirig altalta
4. birdenede def acirig booksale(self) altina nese metod lazimdisa eger o tipde self.ve sair yazirig hazir qoyurug

### sonra baska yerde lazim olanda import staffinfo,Booksale flan edib cagiririg....

# Abstaction Inheritance Polimorfism ve Encapsulation movzusu haqqinda arasdirma
# ABSTRACTION as abs
### abs odurki...html de ki firewall kimi birseydir bir iwin gormezden evvel planin qurulmasi yeni ona vereceyimiz esas hisselerin onceden qurulmasidir....dieyki bir sirket yazacig biz bunu dusunuruyki, wirketde ne olur? isci olur mudur olur marketoloq olur beynelxalq elaqeler wobesi olur ve sair...bu anlayis abs anlayiisidir....BU BIR ANLAYISDIR TETBIQI FORMASI YOXDU

# Encapsulation as enc
### enc anlayisi demey olarki hem nezeri anlayisdi hem tetbiqi anlaayisdi __ ikidenen altdan xett qoyulur parametrin onuneki bildirilsin ki zehmet olmasa buna deyme yaniki o demekdirki bunu kapsula almisam bunu deyisme...nefes almis olmasi funksiasi kimi deyismir hecvaxt meselen __nefes almasi bele birsey yazirigki bunu bizden sora yazacag back ve ya ozmuz ele bile kki buna deymey olmaz

# Inheritance as inh
### inh anlayisi wecere anlayisi kimi birseydir yeni ki meselen babanin familyasi alievdir atada day aliyev yazmaga ehtiac yoxdu ovladidir onsuz onun kod yigni olmasin deye hemcinin sora babanin familyasin deyisende atada avto deyissin deye inherit verirsen ona ki onann gotursun familyasini yene qalan methodlarini yaz gedsinxasietini falan ama ovladidi deye yeni subclassi sayilir deye onun familyasini goturur rahatdignan.... meselen 
class Baba:
    soyad='Haciyev'


class Ata(Baba):
    genetika='Gerizekali'
    
class Ovlad(Ata):
    ad='Memmed'
    

o=Ata()
o.soyad ddeyende output burda atasinin familyasini verir arti

# Poplymorphism as pop
### pop anlayisi inherit anlayisnin davami kimidir...cox cesitliliy qatan birseydir ve tetbiqidir meselen yene aileden yola cixsag inherit de eger yuxaridan atasinin familyasini goture bilirdise bir class burda artiq ona gelen deyeri deyisdire de biliriy....yeni ki meselen alirig deyeri ve ozmuzden elave qatirig yene aileden yola cixsag bunu deye bilerikki meselen atanin familyasi alievdir oglan ovladin familyasida aliyevdir ama qiz ovladi ucun metod yazanda Azerbaycanda qadin soyadlarinda A elavesi olur da meseelen....o a ni elave elemey popdur....kod uzerinde tetbiqini halhazirda
class Baba:
    soyad='Haciyev'

class Ata(Baba):
    genetika='Gerizekali'
    ovladqiz=soyad+a
    
class oglanOvlad(Ata):
    ad='Memmed'

class qizOvlad(Ata):
    ad='xanim'
    if qizOvlad()=ovladqiza
        return ovladqiz

### tetbiqiini hele tam bilmirem sehv yazmis olduguma eminem 



# INitin ferqli yerlerde isledilmesi men bele basa dusduyum qederi super classi istifade edend eolur baska numune tapmadim

# prosedural proqramlama ile oop ferqi 
### OOP ve Prosed??rel Programlama aras??ndaki temel fark, Prosed??rel Programlaman??n oda????n??n programlama g??revini bir de??i??kenler ve alt yordamlar koleksiyonuna b??lmek iken, OOP'nin odak noktas?? programlama g??revini verileri kaps??lleyen nesnelere b??lmektir. ve y??ntemler. En dikkate de??er fark, Prosed??rel Programlaman??n do??rudan veri yap??lar?? ??zerinde i??lem yapmak i??in prosed??rleri kullan??rken, OOP'nin verileri ve y??ntemleri bir araya toplayaca???? ve b??ylece bir nesnenin kendi verileri ??zerinde ??al????aca???? olabilir. ??simlendirme, prosed??r, mod??l, prosed??r ??a??r??s?? ve Prosed??rel Programlamadaki de??i??ken s??z konusu oldu??unda, OOP'de s??ras??yla y??ntem, nesne, mesaj ve ??znitelik olarak an??l??r.

# funksional proqramlama ile oop ferqi
### Farklar Neler?
### Tan??mlama Hususundaki Fark:
Fonksiyonel programlama, fonksiyonlar??n de??er almas?? ??zerinde durur.
Nesne y??nelimli programlama, nesne konsepti ??zerine temellendirilmi??tir.

Veri Hususundaki Fark:
Fonksiyonel programlamada immutable veri kullan??l??r.
Nesne y??nelimli programlamada mutable veri de immutable veri de kullan??l??r.

State Hususundaki Fark:
Fonksiyonel programlama stateless bir programlama modelidir.
Nesne y??nelimli programlama ise stateful bir programlama modelidir.

Programlama Modeli Hususundaki Fark:
Fonksiyonel programlamada deklaratif (declarative) programlama modeli takip edilir.
Nesne y??nelimli programlamada imperatif (imperative) programlama modeli takip edilir.

Paralel Programlama Hususundaki Fark:
Fonksiyonel programlama, paralel programlamay?? destekler.
Nesne y??nelimli programlama, paralel programlamay?? desteklemez.

Manip??lasyon Birimi Hususundaki Fark:
Fonksiyonel programlamada birincil manip??lasyon birimi fonksiyondur.
Nesne y??nelimli programlamada birincil manip??lasyon birimi nesnedir.

Ko??ullu ??fadeler Hususundaki Fark:
Fonksiyonel programlamada ko??ullu ifadeler desteklenmez.
Nesne y??nelimli programlamada ko??ullu ifadeler kullan??labilir.

Ard??????ll??k Hususundaki Fark:
Fonksiyonel programlamada ifadelerin hangi s??rayla ??al????t??r??ld?????? mesele olmaz.
Nesne y??nelimli programlamada ifadelerin hangi s??rayla ??al????t??r??ld?????? genelde ??nemlidir.

??terasyon Hususundaki Fark:
Fonksiyonel programlamada iteratif veri i??in recursion kullan??l??r.
Nesne y??nelimli programlamada iteratif veri i??in loop da recursion da kullan??labilir.

Temel Yaz??l??m Varl??klar?? Hususundaki Fark:
Fonksiyonel programlamada temel yaz??l??m varl??klar?? fonksiyonlar ve de??i??kenlerdir.
Nesne y??nelimli programlamada temel yaz??l??m varl??klar?? metotlar ve nesne ??zellikleridir.

Soyutlama Deste??i Hususundaki Fark:
Fonksiyonel programlamada veri ??zerinde de davran???? ??zerinde de soyutlama do??rudan m??mk??nd??r.
Nesne y??nelimli programlamada do??rudan soyutlama ancak veri ??zerinde m??mk??nd??r.

Odak Noktas?? Hususundaki Fark:
Fonksiyonel programlamada deklaratif programlaman??n bir gere??i olarak ana odak noktas?? ne yap??yor oldu??umuzdur.
Nesne y??nelimli programlamada imperatif programlaman??n bir gere??i olarak ana odak noktas?? nas??l yap??yor oldu??umuzdur.

B??y??k Veri (Big-Data) ????leme Performans?? Hususundaki Fark:
Fonksiyonel programlamada b??y??k veri i??leme performans?? nisbeten y??ksektir.
Nesne y??nelimli programlamada b??y??k veri i??leme performans?? nisbeten d??????kt??r.

Kullan??m Alan?? Hususundaki Fark:
Fonksiyonel programlama, nisbeten, az ??ey ??? ??ok operasyon s??z konusu oldu??unda tercih edilir.
Nesne y??nelimli programlama, nisbeten, ??ok ??ey ??? az operasyon s??z konusu oldu??unda tercih edilir.

Fonksiyonel Programlaman??n Dezavantajlar?? Neler?
Koda i??levsel bir bak???? a????s??ndan yakla??mak ger??ekten farkl?? bir zihniyet gerektirir. Nesne y??nelimli terimlerle d??????nmek ger??ek hayat??n bir taklidi ve soyutlamas?? oldu??u i??in kolayken, fonksiyonel programlama tamamen d??z veri manip??lasyonu ile ilgilidir. Bir ger??ek d??nya senaryosunu d??z veri ve sade operasyonlara d??n????t??rmek fazladan d??????nmeyi gerektirebilir. Sistematik, nisbeten, ger??ek d??nyadakine daha uzak olacakt??r.

Nesne Y??nelimli Programlaman??n Dezavantajlar?? Neler?
Nesne y??nelimli programlamada, i?? yapt??ran kod bloklar??na yeniden kullan??labilirlik kazand??rmak zordur. Yeniden kullan??labilirlik sa??lanmas??n??n m??mk??n olmad??????na kat??lm??yorum ??ahsen. Fakat dolayl?? y??ntemlerle halledilebildi??i nettir. Global fonksiyonu metot ile wrap etmek, statik metodu metot ile wrap etmek, manuel metot bind etmek, soyut s??n??f metodu kullanmak (tavsiye edilmez), trait s??n??f?? kullanmak bu dolayl?? y??ntemlerden birka????d??r.

????levsellik hem hiyerar??ik yap??da olabildi??i hem de enkaps??le olabildi??i i??in operasyonla ba?? etmek nisbeten daha karma????kt??r ve bununla birlikte verimlilik bir miktar d??????k olur. Fonksiyonel programlamadaki i??levsellik ise genellikle flat???tir. ???Platformda engebe yoktur??? da denebilir.

OOP???de temsil m??him oldu??u i??in b??y??k mimarilerde temsil edilen nesnenin fazlal??????, u??uk karma??aya yol a??abilir.

Sonu?? Olarak
Nesne y??nelimli diller, nesneler ??zerinde sabit bir i??lem k??meniz oldu??unda iyidir ve kodunuz geli??tik??e, ??ncelikle yeni ??eyler eklersiniz. Bu, mevcut metotlar?? implemente eden yeni s??n??flar eklenerek ger??ekle??tirilebilir ve mevcut s??n??flar yaln??zla??t??r??l??r.

Fonksiyonel diller, sabit ??eyler k??mesine sahip oldu??unuzda iyidir ve kodunuz geli??tik??e, ??ncelikle mevcut ??eylere yeni operasyonlar eklersiniz. Bu, mevcut veri tipleri ile i??leyen yeni fonksiyonlar eklenerek ger??ekle??tirilebilir ve mevcut fonksiyonlar yaln??zla??t??r??l??r.

Basit??e ifade etmek gerekirse, farkl?? ??er??eveler i??inde ??al??????l??yorsa OOP her ??eyi paketlenmi?? olarak tutmak ve istenmeyen harici kullan??mlardan korumak i??in m??kemmel bir y??ntem iken fonksiyonel programlama, uygulama karma????kl??k ihtiva ediyorsa iyidir.

Nesne odakl?? d??????nme back-end???de i??e yarar. ????nk?? ??o??u zaman sonraki ??er??eveye paslamak i??in bir ??eyler in??a etmek, bilinmeyene g??ndermeden ??nce paketlemek, sarmalamak gerekir.

Fonksiyonel programlamada ve nesne y??nelimli programlamada verileri manip??le etmek ve depolamak i??in farkl?? y??ntemler kullan??l??r. Fonksiyonel programlamada, veriler nesnelerde saklanmaz, sadece fonksiyonlar olu??turularak d??n????t??r??lebilir. Nesne y??nelimli programlamada, veriler nesnelerde saklan??r. Nesne y??nelimli programlama yayg??n olarak kullan??l??r ve ayn?? zamanda ba??ar??l??d??r da.

Nesne y??nelimli programlamada, kal??t??m d??zeylerini art??r??rken nesneleri korumak ger??ekten zordur. Bu, ayn?? zamanda kaps??lleme ilkesini de bozar ve hatta tamamen mod??ler olmaktan ????kar??r. Fonksiyonel programlamada nesne kullan??ld??????nda ise, fonksiyonlar?? ??al????t??rmak i??in her zaman yeni bir nesne gerekir ve uygulamay?? ??al????t??rmak ??ok fazla belle??e mal olabilir

Paradigmalar??, yakla????mlar??, teknikleri, y??ntemleri kullan??m alan??na g??re se??mek laz??m. Se??eneklerinizi biliyorsan??z ne yapt??????n??z?? bilmenize ??ok yak??ns??n??z demektir. 


