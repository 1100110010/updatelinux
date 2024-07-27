#Gerekli kütüphanelerimizi ekliyoruz.
from os import system
from time import sleep
import sys

sleep(1)
#Uçbirim ekranını temizleyip program içerisinde kullanacağımız değerlere varsayılan olarak '0' değerini atıyoruz.
system("clear")
sistem = 0
brave = 0
firefox = 0
tuxedo = 0
sleep(1)
#15-55. satırlar ile klavye animasyonu süsü verilmiş bildirgemizi ekrana yazdırıyoruz. 
line_1 = """Merhabalar.""" + "\n"
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.8)

line_2 = """Lütfen programı yönetici izinleri ile başlatmayı unutmayın.""" + "\n"
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.8)

line_3 = """Programı tamamen izlemenize, takip etmenize gerek yok.""" + "\n"
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.4)

line_3 = """Seçim anlarında tercih vermeniz yeterli olacaktır.""" + "\n"
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(1)

line_3 = """Teşekkür ederiz."""
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(1)

line_4 = " <3" + "\n"
for x in line_4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(2)
#Kullanıcının bildirgeyi sınırlama olmaksızın okuması için istediği zaman geçmesine olanak tanıyoruz.
input("Devam etmek için 'enter' tuşuna basınız: ")
system("clear")
#60-104. satırlar arasında kullanıcının istekleri babındaki girdileri alıyoruz.
soru = input("Sistemi güncellemek ister misiniz? (E/H): ")
if soru == "e":
    sistem = 1
elif soru == "E":
    sistem = 1
elif soru == "y":
    sistem = 1
elif soru == "Y":
    sistem = 1

system("clear")
soru = input("Brave tarayıcısını indirmek ister misiniz? (E/H): ")
if soru == "e":
    brave = 1
elif soru == "E":
    brave = 1
elif soru == "y":
    brave = 1
elif soru == "Y":
    brave = 1

system("clear")
soru = input("Firefox tarayıcısını silmek ister misiniz? (E/H): ")
if soru == "e":
    firefox = 1
elif soru == "E":
    firefox = 1
elif soru == "y":
    firefox = 1
elif soru == "Y":
    firefox = 1

system("clear")
soru = input("""Tuxedo Yönetim Merkezi indirme betiği varsayılan olarak Jammy sürümüne ayarlıdır.
Eğer Jammy sürümü kullanmıyorsanız dosyalardan betiği kendinizce ayarlayabilir,
veya dilerseniz bu etabı atlayıp işlemi elle gerçekleştirebilirsiniz.
Tuxedo Yönetim Merkezini indirmek ister misiniz? (E/H): """)
if soru == "e":
    tuxedo = 1
elif soru == "E":
    tuxedo = 1
elif soru == "y":
    tuxedo = 1
elif soru == "Y":
    tuxedo = 1
system("clear")
#Kullanıcının seçimleri doğrultusunda gerekli betikleri çalıştırıyoruz.
if sistem == 1:
    system("cd betikler && bash sistem.sh")
if brave == 1:
    system("cd betikler && bash tarayıcı.sh")
if firefox == 1:
    system("cd betikler && bash firefox.sh")
if tuxedo == 1:
    system("cd betikler && bash tuxedo.sh")
