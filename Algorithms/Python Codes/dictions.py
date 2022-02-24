from hebib import countries
from re import I

def FindCity(cityname):
    olkeler = list(countries.keys())
    seherler = list(countries.values())
    for olke in range(len(olkeler)):
        for seher in range(len(seherler)):
            if cityname in seherler[seher] and olke==seher:
                print(f'{cityname} -' ,olkeler[olke])


FindCity('Baku')
  # seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin


