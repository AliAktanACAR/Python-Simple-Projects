
print("""
***************************************
Basit Hesap Makinasına hoşgeldiniz
************************************** *
toplama işlemi yapmak için 1'e basınız *
çıkarma işlemi yapmak içi 2'ye basınız *
çarpma  işlemi yapmak için 3'e basınız *
bölme   işlemi yapmak için 4'e basınız *
kare alma isşlemi yapmak için 5'e basınız *
************************************** *
""")
islem=str(input("işlem seçiniz: "))

if islem=="1":
    sayi1=int(input("birinci sayıyı giriniz : "))
    sayi2=int(input("ikinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1+sayi2)

if islem=="2":
    sayi1=int(input("birinci sayıyı giriniz : "))
    sayi2=int(input("ikinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1-sayi2)

if islem=="3":
    sayi1=int(input("birinci sayıyı giriniz : "))
    sayi2=int(input("ikinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1*sayi2)

if islem=="4":
    sayi1=int(input("birinci sayıyı giriniz : "))
    sayi2=int(input("ikinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1/sayi2)

if islem=="5":
    sayi1=int(input("Birinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1*sayi1)

if islem=="6":
    sayi1=int(input("Birinci sayıyı giriniz : "))
    print("Sonuç : ",sayi1*sayi1*sayi1)






