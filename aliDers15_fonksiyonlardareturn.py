# fonksiyonlarda return
#bir fonksiyonun değer döndürmesini sağlayan return ifadesi
#return ifadesi fonksiyonun işlemi bittikten sonra çağırıldığı yere değer döndürmesi anlamını taşır
"""
def toplama(a,b,c): #birinci foksiyon
    print("toplamları = ",a+b+c)

toplama(12,3,5)
toplam=toplama(12,3,5)

def ikiylecarp(b):
    print("ikiyle çarpılmş hali:",b*2)

ikiylecarp(12)
#ikiylecarp(toplam)
########################################################################################################################

def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a):
    return a*2
toplam=toplama(3,5,2)
#toplam=26
print(toplam)
print("sonuç: ",ikiylecarp(toplam))

def uclecarp(a):
    print("1. fonksiyon çalıştı")
    return a*3

def ikiyletopla(a):
    print("2. fonksiyon çalıştı")
    return a+2

def dordebol(a):
    print("3. fonksiyon çalıştı")
    return a/4
print(uclecarp(2))
print(ikiyletopla(2))
print(dordebol(2))
print(dordebol(ikiyletopla(uclecarp(2)))) #2

#return ifadesi ile fonksiyon sona erer, return herhangi bir işlem çalıştırılmaz

def toplama(a,b,c):
    print("toplama fonksiyonu")
    return
print(toplama(1,2,3)) # herhangi bir değer döndürmez

def toplama(a,b,c):
    print("toplama fonksiyonu :",a+b+c)
    return
toplama(1,2,3)
################################################################################

#parametre olan fonksiyonlar
def toplama(sayi1,sayi2):
    return sayi1+sayi2
print("sonuç = ",toplama(2,8))

#parametrelere değer önceden değer atabiliyoruz
def toplama(sayi1=6,sayi2=6):
    return sayi1+sayi2
print("sonuç = ",toplama())


#değer verdiğimiz parametreleri değiştirebiliriz
def toplama(sayi1=6,sayi2=6): #default parametreler oluyor
    return sayi1+sayi2
print("sonuç = ",toplama(3,5))

#parametreleri kullanıcıdan alabiliriz
def toplama(sayi1,sayi2):
    return sayi1+sayi2
sayi1=int(input("Birinci sayıyı giriniz : "))
sayi2=int(input("İkinci sayıyı giriniz : "))

print("sonuç : ",toplama(sayi1,sayi2))
"""
##############################################################################
### HESAP MAKİNASİ ###

# Toplama İşlemi
def toplama(x,y):
    print("İŞLEMİN SONUCU :\t{}\t+\t{}\t=\t{}\t".format(x,y,x+y))
    return x+y

print(toplama(3,5))

# Çıkartma İşlemi
def çıkartma(x,y):
    print("İŞLEMİN SONUCU :\t{}\t+\t{}\t=\t{}\t".format(x,y,x-y))
    return x-y

print(çıkartma(3,5))
# Bölme İşlemi
def bölme(x,y):
    print("İŞLEMİN SONUCU :\t{}\t-\t{}\t=\t{}\t".format(x,y,x/y))
    return x/y

print(bölme(3,5))
#çarpma
def çarpma(x,y):
    print("İŞLEMİN SONUCU :\t{}\t/\t{}\t=\t{}\t".format(x,y,x*y))
    return x*y

print(çarpma(3,5))
def kare(x):
    print("İŞLEMİN SONUCU :\t{}\t=\t{}\t".format(x,x*x))
    return x*x

print(kare(5))

while True:
    print("1.Toplama İşlemi")
    print("2.Çıkartma İşlemi")
    print("3.Bölme İşlemi")
    print("4.Çarpma İşlemi")
    print("5.Çıkış")
    islem_secim=int(input("Yapmak istediğiniz işlemi seçiniz : "))

    if islem_secim==1:
        sayi1=float(input("1.Sayıyı Girin"))
        sayi2=float(input("2.Sayıyı Girin"))
        toplama(sayi1,sayi2)
    elif islem_secim==2:
        sayi1=float(input("1.Sayıyı Girin"))
        sayi2=float(input("2.Sayıyı Girin"))
        çıkartma(sayi1,sayi2)
    elif islem_secim==3:
        try:  #bekle orda bir hata var try, hatalar için bir kod blodğu test etmemizi sağlar #bölen sayı 0 olamaz, hatayı yakalamamzı gerekir
            sayi1 = float(input("1.Sayıyı Girin"))
            sayi2 = float(input("2.Sayıyı Girin"))
            çarpma(sayi1, sayi2)
        except ZeroDivisionError:
            print("SAYI 0'A BÖLÜNEMEZ")
    # expection 0 hatasını işlememizi sağlar
    elif islem_secim==4:
        sayi1=float(input("1.Sayıyı Girin"))
        sayi2=float(input("2.Sayıyı Girin"))
        çarpma(sayi1,sayi2)
    elif islem_secim==6:
        sayi1=float(input("1.Sayıyı Girin"))
        kare(sayi1)
    else:
        print("program sonlandı")
        break


