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
### OOP ve Prosedürel Programlama arasındaki temel fark, Prosedürel Programlamanın odağının programlama görevini bir değişkenler ve alt yordamlar koleksiyonuna bölmek iken, OOP'nin odak noktası programlama görevini verileri kapsülleyen nesnelere bölmektir. ve yöntemler. En dikkate değer fark, Prosedürel Programlamanın doğrudan veri yapıları üzerinde işlem yapmak için prosedürleri kullanırken, OOP'nin verileri ve yöntemleri bir araya toplayacağı ve böylece bir nesnenin kendi verileri üzerinde çalışacağı olabilir. İsimlendirme, prosedür, modül, prosedür çağrısı ve Prosedürel Programlamadaki değişken söz konusu olduğunda, OOP'de sırasıyla yöntem, nesne, mesaj ve öznitelik olarak anılır.

# funksional proqramlama ile oop ferqi
### Farklar Neler?
### Tanımlama Hususundaki Fark:
Fonksiyonel programlama, fonksiyonların değer alması üzerinde durur.
Nesne yönelimli programlama, nesne konsepti üzerine temellendirilmiştir.

Veri Hususundaki Fark:
Fonksiyonel programlamada immutable veri kullanılır.
Nesne yönelimli programlamada mutable veri de immutable veri de kullanılır.

State Hususundaki Fark:
Fonksiyonel programlama stateless bir programlama modelidir.
Nesne yönelimli programlama ise stateful bir programlama modelidir.

Programlama Modeli Hususundaki Fark:
Fonksiyonel programlamada deklaratif (declarative) programlama modeli takip edilir.
Nesne yönelimli programlamada imperatif (imperative) programlama modeli takip edilir.

Paralel Programlama Hususundaki Fark:
Fonksiyonel programlama, paralel programlamayı destekler.
Nesne yönelimli programlama, paralel programlamayı desteklemez.

Manipülasyon Birimi Hususundaki Fark:
Fonksiyonel programlamada birincil manipülasyon birimi fonksiyondur.
Nesne yönelimli programlamada birincil manipülasyon birimi nesnedir.

Koşullu İfadeler Hususundaki Fark:
Fonksiyonel programlamada koşullu ifadeler desteklenmez.
Nesne yönelimli programlamada koşullu ifadeler kullanılabilir.

Ardışıllık Hususundaki Fark:
Fonksiyonel programlamada ifadelerin hangi sırayla çalıştırıldığı mesele olmaz.
Nesne yönelimli programlamada ifadelerin hangi sırayla çalıştırıldığı genelde önemlidir.

İterasyon Hususundaki Fark:
Fonksiyonel programlamada iteratif veri için recursion kullanılır.
Nesne yönelimli programlamada iteratif veri için loop da recursion da kullanılabilir.

Temel Yazılım Varlıkları Hususundaki Fark:
Fonksiyonel programlamada temel yazılım varlıkları fonksiyonlar ve değişkenlerdir.
Nesne yönelimli programlamada temel yazılım varlıkları metotlar ve nesne özellikleridir.

Soyutlama Desteği Hususundaki Fark:
Fonksiyonel programlamada veri üzerinde de davranış üzerinde de soyutlama doğrudan mümkündür.
Nesne yönelimli programlamada doğrudan soyutlama ancak veri üzerinde mümkündür.

Odak Noktası Hususundaki Fark:
Fonksiyonel programlamada deklaratif programlamanın bir gereği olarak ana odak noktası ne yapıyor olduğumuzdur.
Nesne yönelimli programlamada imperatif programlamanın bir gereği olarak ana odak noktası nasıl yapıyor olduğumuzdur.

Büyük Veri (Big-Data) İşleme Performansı Hususundaki Fark:
Fonksiyonel programlamada büyük veri işleme performansı nisbeten yüksektir.
Nesne yönelimli programlamada büyük veri işleme performansı nisbeten düşüktür.

Kullanım Alanı Hususundaki Fark:
Fonksiyonel programlama, nisbeten, az şey – çok operasyon söz konusu olduğunda tercih edilir.
Nesne yönelimli programlama, nisbeten, çok şey – az operasyon söz konusu olduğunda tercih edilir.

Fonksiyonel Programlamanın Dezavantajları Neler?
Koda işlevsel bir bakış açısından yaklaşmak gerçekten farklı bir zihniyet gerektirir. Nesne yönelimli terimlerle düşünmek gerçek hayatın bir taklidi ve soyutlaması olduğu için kolayken, fonksiyonel programlama tamamen düz veri manipülasyonu ile ilgilidir. Bir gerçek dünya senaryosunu düz veri ve sade operasyonlara dönüştürmek fazladan düşünmeyi gerektirebilir. Sistematik, nisbeten, gerçek dünyadakine daha uzak olacaktır.

Nesne Yönelimli Programlamanın Dezavantajları Neler?
Nesne yönelimli programlamada, iş yaptıran kod bloklarına yeniden kullanılabilirlik kazandırmak zordur. Yeniden kullanılabilirlik sağlanmasının mümkün olmadığına katılmıyorum şahsen. Fakat dolaylı yöntemlerle halledilebildiği nettir. Global fonksiyonu metot ile wrap etmek, statik metodu metot ile wrap etmek, manuel metot bind etmek, soyut sınıf metodu kullanmak (tavsiye edilmez), trait sınıfı kullanmak bu dolaylı yöntemlerden birkaçıdır.

İşlevsellik hem hiyerarşik yapıda olabildiği hem de enkapsüle olabildiği için operasyonla baş etmek nisbeten daha karmaşıktır ve bununla birlikte verimlilik bir miktar düşük olur. Fonksiyonel programlamadaki işlevsellik ise genellikle flat‘tir. “Platformda engebe yoktur” da denebilir.

OOP’de temsil mühim olduğu için büyük mimarilerde temsil edilen nesnenin fazlalığı, uçuk karmaşaya yol açabilir.

Sonuç Olarak
Nesne yönelimli diller, nesneler üzerinde sabit bir işlem kümeniz olduğunda iyidir ve kodunuz geliştikçe, öncelikle yeni şeyler eklersiniz. Bu, mevcut metotları implemente eden yeni sınıflar eklenerek gerçekleştirilebilir ve mevcut sınıflar yalnızlaştırılır.

Fonksiyonel diller, sabit şeyler kümesine sahip olduğunuzda iyidir ve kodunuz geliştikçe, öncelikle mevcut şeylere yeni operasyonlar eklersiniz. Bu, mevcut veri tipleri ile işleyen yeni fonksiyonlar eklenerek gerçekleştirilebilir ve mevcut fonksiyonlar yalnızlaştırılır.

Basitçe ifade etmek gerekirse, farklı çerçeveler içinde çalışılıyorsa OOP her şeyi paketlenmiş olarak tutmak ve istenmeyen harici kullanımlardan korumak için mükemmel bir yöntem iken fonksiyonel programlama, uygulama karmaşıklık ihtiva ediyorsa iyidir.

Nesne odaklı düşünme back-end‘de işe yarar. Çünkü çoğu zaman sonraki çerçeveye paslamak için bir şeyler inşa etmek, bilinmeyene göndermeden önce paketlemek, sarmalamak gerekir.

Fonksiyonel programlamada ve nesne yönelimli programlamada verileri manipüle etmek ve depolamak için farklı yöntemler kullanılır. Fonksiyonel programlamada, veriler nesnelerde saklanmaz, sadece fonksiyonlar oluşturularak dönüştürülebilir. Nesne yönelimli programlamada, veriler nesnelerde saklanır. Nesne yönelimli programlama yaygın olarak kullanılır ve aynı zamanda başarılıdır da.

Nesne yönelimli programlamada, kalıtım düzeylerini artırırken nesneleri korumak gerçekten zordur. Bu, aynı zamanda kapsülleme ilkesini de bozar ve hatta tamamen modüler olmaktan çıkarır. Fonksiyonel programlamada nesne kullanıldığında ise, fonksiyonları çalıştırmak için her zaman yeni bir nesne gerekir ve uygulamayı çalıştırmak çok fazla belleğe mal olabilir

Paradigmaları, yaklaşımları, teknikleri, yöntemleri kullanım alanına göre seçmek lazım. Seçeneklerinizi biliyorsanız ne yaptığınızı bilmenize çok yakınsınız demektir. 


