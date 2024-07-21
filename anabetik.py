from os import system
from time import sleep
import sys

#system("clear")
def exit_program():
    print("Exiting the program...")
    sys.exit(0)

sleep(3)
line_1 = """Merhabalar.""" + "\n"
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.8)

line_2 = """Lütfen programı yönetici izinleri ile başlatıp, terminali tam ekran yapmayı unutmayın.""" + "\n"
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.8)

line_3 = """F11'e tıklamanıza gerek yok."""
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.4)

line_3 = """ Ekranı büyütüp bütün ekranı kaplamasını sağlamanız yeterli olacaktır.""" + "\n"
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

line_4 = " <3"
for x in line_4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.02)
sleep(0.5)
print("\n")
soru = input("Programı gerekli koşullar altında başlattınız mı? (E/H")
if not soru ==  "e"  or "E" or "y" or "Y":
    exit_program()

print("deneme")
