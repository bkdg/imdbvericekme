import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

imdb = 'https://www.imdb.com/chart/top/'#link
r = requests.get(imdb)#site ile bağlantı

soup  = BeautifulSoup(r.content,"html.parser") #site kaynağını görüntülüyor(binevi öğeyi denetle)

gelen_veri = soup.find_all("table",{"class":"chart full-width"})#site kaynağında "table class chart full-width" arıyor.

filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents) -2 ]#gelen_veri bize 3 nesne veriyor,biz tbodye için sondan ikinci olanı (bkz:-2) yani tbodyi seçiyoruz.


filmtablosu = filmtablosu.find_all("tr")#tbody içinde tryi seçiyoruz

for film in filmtablosu:#döngü
    filmbasliklari = film.find_all("td",{"class":"titleColumn"})#Başlıları alıyoruz,'film' heryeri geizyor
    rating = film.find_all("td",{"class":"ratingColumn"})#IMDB Puanını alıyoruz.
    
    filmismi = filmbasliklari[0].text.replace("\n","")#text halini alıyoruz,liste 1 elemanlı olduğu için 0.indexten başlıyoruz burada aslında her eleman bir 'film',bu sebeple tek tek film isimlerini göreceğiz.
    rate = rating[0].text.replace("\n","")#Aynı şekilde IMDB Puanını text halinde görmek için.
    print(filmismi,"IMDB",rate,"⭐")
    print("****************")
