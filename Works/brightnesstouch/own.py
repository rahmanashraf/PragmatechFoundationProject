from bs4 import BeautifulSoup as bs
import requests


url= "http://slimhamdi.net/tunis/dark/index.html"
dosyatype= ".pdf"
def duzelt(url):
    return bs(requests.get(url).text, 'html.parser')

for link in duzelt(url).find_all('a'):
    linkim=link.get('href')
    if dosyatype in linkim:
        dosya_adi=linkim.split('/')[-1]
        with open(dosya_adi, 'wb') as dosya:
            cevap=requests.get(linkim)
            dosya.write(cevap.content)

