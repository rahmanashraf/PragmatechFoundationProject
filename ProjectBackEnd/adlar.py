adlar=[
    'Fezail',
    'Rehman',
    'Elmar',
    'Sebuhi',
    'Aysel',
    'Murad',
    'Vesile',
    'Ravi'
]

# Butun adlari ekrana cap eden metod yazin adlariGoster()-+++++++++
# Listin cut yerde duran elementlerini gosteren metod yazin cutYerdekiler()-+++++++++++
# Listi elifba sirasina gore siralayan metod yazin listiSirala() -+++++++++++
#Daxilində e herfi olan adları ekrana cap edən metod yazin
#Son hərfi i olan adlari ekrana cap eden metod yazin
#Hərf sayi eyni olan nece ad oldugunu ekrana cap edin

def adlariGoster(adlar):
    for ad in adlar:
        print(ad)

adlariGoster(adlar)

def cutyerdekiler():
    for i in adlar:
        x=adlar.index(i)
        if x%2==0:
            return(x)
            
        

cutyerdekiler() 

def listisirala():
    adlar.sort()
    adlariGoster(adlar)


listisirala()

def eherfintapan():
    for abdul in adlar:
        if abdul.find("e")!=-1:
            print(f'{abdul} e herfi var')
            
        


eherfintapan()

def sonherfiIolsun():
    for soni in adlar:
        x=soni[-1:]
        if x=="i":
            print(soni)


sonherfiIolsun()

def herfsayieyni():
    for herf in adlar:
        c=len(herf)
        
        
            


herfsayieyni()