# while döngüleri
# bu derste while döngülerini öğrenmeye başlıyoruz
# while döngüleri belli bir koşul sağlanmadığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder
"""

    while(koşul):
        islem1
        islem2
        islem3



"""
# döngüde 1 değerini ekrana yazdırma
"""
i=0

while(i<10):
    print("i'nin değeri",i)
    i+=1 #koşulun false değer dönmesi için artırma yada azaltma yapmıyor

k=0
while(k<20):
    print("k'nin değeri",k)
    k+=2

ali=0
while(ali<9):
    print("yakışıklı ali")
    ali+=1

# liste ile indeks üzerinde gezinme
liste=[1,2,3,4,5]
ada=0
while(ada< len(liste)):
    print("indeks",ada,"eleman",liste[ada])
    ada+=1

# Faktöriyel hesaplama
# 3!=3*2*1=6
# 6!6*5*4*3*2*1=720
x=6
sayi=1
while(x>1):
    sayi=sayi*x
    x-=1
print(sayi)
x=int(input("faktoriyel için sayı giriniz:"))
sayi=1
while(x>1):
    sayi=sayi*x
    x-=1
print(sayi)

def calculationFactorial():
    number=int(input("Lütfen faktoriyelini hesaplamak istediğiniz sayıyı giriniz:"))
    factorial=1 # 0! faktoriyel= 0!= 1!/1 . bu nedenle ilk sayıya 1 ataması yapıyoruz
    if (number>=0):
        for i in range(1, number+1):
            factorial=factorial*i
        print("istediğiniz sayının faktoriyali",factorial)
    else:
        print("negatif sayının faktoriyalı olmaz")
calculationFactorial()
"""
# gelişmiş hesap makinası

giris="""
(1) +
(2) -
(3) x
(4) /
(5) karesini hesapla
(6) karekökünü hesapla 
(7) faktoriyel hesaplama
"""

print(giris)

while True: #aksi belirtilmediği halde sonsuza kadar çalışmaya devam eder
    soru=(input("yapmak istediğiniz işlem numarasını girin. (Çıkmak için q girin):"))

    if soru=="q":
        print("ÇIKILIYOR...")
        break # ingilizce de kırmak kopmak anlamına gelir

    elif soru=="1":
        sayı1=int(input("toplama için ilk sayıyı girin:"))
        sayı2 = int(input("toplama için ikinci sayıyı girin:"))
        print(sayı1," + ", sayı2, " = ",sayı1+sayı2)

    elif soru=="2":
        sayı1=int(input("çıkarma için ilk sayıyı girin:"))
        sayı2 = int(input("çıkarma için ikinci sayıyı girin:"))
        print(sayı1," - ", sayı2, " = ",sayı1-sayı2)

    elif soru=="3":
        sayı1=int(input("çarpma için ilk sayıyı girin:"))
        sayı2 = int(input("çarpma  için ikinci sayıyı girin:"))
        print(sayı1," * ", sayı2, " = ",sayı1*sayı2)

    elif soru=="4":
        sayı1=int(input("bölme için ilk sayıyı girin:"))
        sayı2 = int(input("bölme için ikinci sayıyı girin:"))
        print(sayı1," / ", sayı2, " = ",sayı1/sayı2)

    elif soru=="5":
        sayı1=int(input("karesi için ilk sayıyı girin:"))
        print(sayı1," * ", sayı1, " = ",sayı1*sayı1)# sayı1**2

    elif soru=="6":
        sayı1=int(input("karekök için ilk sayıyı girin:"))
        print(sayı1," * ", sayı1, " = ",sayı1**0.5)

    elif soru=="7":
        sayı1= int(input("faktoriyel için sayı giriniz:"))
        sayi = 1
        while (sayı1 > 1):
            sayi = sayi * sayı1
            sayı1 -= 1
        print(sayi)

    else:
        print("Aşağıdaki seçeneklerden birini giriniz :", giris)


