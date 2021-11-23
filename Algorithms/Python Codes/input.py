# seninadinnedir=input("x: ")
# seninyasinkacoglum=input("y: ")
# print(seninadinnedir+seninyasinkacoglum)

"""bir masin neche km yol gedibse onu mil olaraq print ele
mil=km/1.6"""

km=int(input("Nechke km getmisen atam?: "))
suret=int(input("Neche suretnen gedmisen?: "))

ekvivalent=1.6
zaman=km/suret
miles=km/ekvivalent

print(f'Siz {km} kilometr yol getmekle {miles} mil yol qet etmis oldunuz')
print('Siz'+' '+str(km)+' '+'kilometrlik yolu'+' '+str(suret)+' '+'km/saat suret ile surseniz gedeceyiniz menzile'+' '+str(zaman)+'saat muddetinde catmis olarsiniz')

