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


