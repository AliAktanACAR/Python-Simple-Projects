#hesap makinası
"""
# print(*****************************************
Hesap Makinası Programına Hoşgeldiniz
    1.Toplama İşlemi
    2.Çıkarma İşlemi
    3.Çarpma İşlemi
    4.Bölme İşlmei
****************************************
)
a=int(input("Birini sayıyı giriniz :")) #birinci sayıyı alıyoruz
b=int(input("İkinci sayıyı giriniz :")) #ikinci sayıyı alıyoruz
islem=(input("işlem numarasını giriniz :")) #buna göre koşulu sağlıyoruz

if (islem=="1"):
    print("{} ile {}'nin toplamı {}'dır.".format(a,b,a+b))
elif (islem=="2"):
    print("{} ile {}'nin farkı {}'dır.".format(a,b,a-b))
elif (islem=="3"):
    print("{} ile {}'nin çarpımı {}'dır.".format(a,b,a*b))
elif (islem=="4"):
    print("{} ile {}'nin bölümü {}'dır.".format(a,b,a/b))
else:
    print("Lütfen Geçerli Bir İşlem Seçiniz")
"""
import math
ilkSayi1=(input("Birnici Sayıyı Giriniz :"))
ilkSayi2=(input("İkinci Sayıyı Giriniz :"))
sayi1=float(ilkSayi1) #float methodu girdiğiniz sayının ondalıklı sayı olarak alınmasını sağlar
sayi2=float(ilkSayi2)
islem=input(" İşlemi Giriniz (+,-,*,/,sqrt,log) : ")
if islem=="+":
    sonuc=sayi1+sayi2
elif islem=="-":
    sonuc=sayi1-sayi2
elif islem=="*":
    sonuc=sayi1*sayi2
elif islem=="/":
    sonuc=sayi1/sayi2
elif islem=="sqrt":
    sonuc=math.sqrt(sayi1)
elif islem=="log":
    sonuc=math.log(sayi1)
else:
    print("Geçersiz İşlem")
print("Sonuç = ",sonuc)






