import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
class Register():

    def __init__(self,name="rehman",surname="abdullayev",email="rehman@gmail.com",phone="0502015187",password="rehman",qisamelumat="rehmanun"):
        self.name=name
        self.surname=surname
        self.email=email
        self.phone=phone
        self.password=password
        self.qisamelumat=qisamelumat

    def Username(self):
        self.name=input(str("Adi daxil edin: "))
        if self.name != "" :
            print("duzgundur")
        else:
            print('Bu xana bosh olmaz')

    def Surname_(self):
        self.surname=input(str("Soyadini daxil edin: "))
        if self.surname != "":
            print("duzgundur")
        else:
            print('doldurmaq zeruridir')
    def Mailiyaz(self):
        self.email=input(str("E-mail daxil et: "))
        if (re.search(regex,self.email)):
            print("duz yazdin")
        else:
            print("sehv yazdin")
    
        
    def paSSword(self):
        self.password=input(str("Parolu daxil et: "))
        val = True
        
        if len(self.password) < 8:
            print('Minimum 8 xarakterden ibaret olmalidir qaqash')
            val = False
            
        if len(self.password) > 20:
            print('Maksimum 20 xarakterden ibaret olmalidir')
            val = False
            
        if not any(char.isdigit() for char in self.password):
            print('Daxilinde mutleq bir reqem olmalidir')
            val = False
            
        if not any(char.isupper() for char in self.password):
            print('Minimum bir eded boyuk herf olmalidir.')
            val = False
            
        if not any(char.islower() for char in self.password):
                print('Minimum bir eded kicik herf olmalidir')
                val = False
        if val:
            return val
            

# user=Register("Elmar","Memmedov","jdsjdh@gmail.com","055-445-55-55","12345","Sebuhi")
araba1=Register()
araba1.Username()
araba1.Surname_()
araba1.Mailiyaz()
araba1.paSSword()
