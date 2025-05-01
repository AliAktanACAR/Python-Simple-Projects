# Fonksiyonlar
""" fonksiyon yapısı
def=define (tanımlamak)

def x

def <fonksiyon_ismi> (<argümanlar>): #snake_case
                                     #docstirng: üç tırnak kullanarak açıklama yapılması
                                     #return / print : Ya bir şey bastrılır yada döndürülür
"""

def selamlama():
    print("Merhaba Arkadaş.,.,.,.,")
    print("Nasılsın ?")

selamlama()
selamlama()

#Fonksiyonlar argüman ve parametreler

def selamlama(isim):
    print("Merhaba",isim)
    #print("İsminiz",isim)

selamlama("Mehmet")
selamlama("Ali")
selamlama("Defne")
selamlama("Tuna")
selamlama("Ege")
selamlama("çınar")
selamlama("Team3390")

def my_function(fname):
    print(fname+" çalışkandır")
my_function("Ali")
my_function("Çınar")

def faktoriyel(sayi):
    faktoriyel=1
    if (sayi==0 or sayi==1):
        print(faktoriyel)
    else:
        while(sayi>=1):
            faktoriyel*=sayi
            sayi-=1

        print("faktöriyel",faktoriyel)

faktoriyel(4)
faktoriyel(1)
faktoriyel(0)
faktoriyel(10)


def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Ali","Acar")
# Argüman sayısı bilinmiyorsa, istediğim parametreden önce * eklemem gerekir

def my_function(*kids):
    print("öğrencilerim :"+kids[2])

my_function("Ali","Utku","Ada")

#anahtar kelimeler ile bağımsız değişkenler, = kullanıyoruz

def my_function(child3,child2,child1,child0):
    print("Öğrencilerim :"+child1+child2+child3+child0)
#argümanların sırası önemli dğeildir
#fonksiyonu çağırıyorum

my_function(child1="Utku", child2=" Ali", child3=" Erda", child0=" Çınar")

#Keyfi anahtar kelimeler nasıl kullanılır?

def my_function(**kid):
    print("Soyadınız: "+kid["lname"])
    print("Adınız: "+ kid["fname"])
my_function(fname="Ali",lname="Acar")

#varsayılan parametre değeri

def my_function (country="Türkiye"):
    print("Yaşadğım Ülke : "+country)

my_function("İsviçre")
my_function("Hawaii")
my_function() #default argüman : yaşadığım ülke: Türkiye
my_function("Fransa")
my_function("Moğolistan")

def my_function (country="Türkiye"):
    if country=="Hawaii":
        print("Yaşadığım yer:",country)
    print("Yaşadğım Ülke : "+country)

# bir çok parametreye sahip olmak
def bilgilerigöster(ad="Bilgi yok", soyad="Bilgi yok", numara="Bilgi yok"):
    print("ad:", ad, "soyad:", soyad, "numara:", numara)
    print("ad:",ad,"soyad:",soyad, "numara:",numara,sep=":")


bilgilerigöster()
bilgilerigöster("Ali","ACAR","1885")
bilgilerigöster(numara=1234567890)
bilgilerigöster(ad="Ali",numara="1885")
bilgilerigöster("Ali","ACAR","1885",sep="/")
print(bilgilerigöster("Ali","ACAR","1885",sep=":"))




