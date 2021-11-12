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

# Butun adlari ekrana cap eden metod yazin adlariGoster()
# Listin cut yerde duran elementlerini gosteren metod yazin cutYerdekiler()
# Listi elifba sirasina gore siralayan metod yazin listiSirala() 

def adlariGoster(adlar):
    for ad in adlar:
        print(ad)

adlariGoster(adlar)

def cutyerdekiler():
    for i in adlar:
        x=adlar.index(i)
        if x%2==0:
            print(x)
        

cutyerdekiler() 

def listisirala():
    adlar.sort()
    print(adlar)


listisirala()




