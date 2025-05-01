#if else koşullu durumları
"""

a=2
b=3
c=4
print(a+b+c) #9

a=2
if (a==2):
    print(True)
print("merhaba")


if (koşul): #if bloğu koşul (True) sağlanınca çalışır
    # if bloğu - girintiye dikkat edilmeli
    # yazılan işlemler çalışır
    ...
if (koşul sağlanıyorsa): True dönüyorsa
    (burada yazılanı yap)
elif(alternatif koşul sağlanıyorsa): True dönüyorsa
    (burada yazılanı yap)
elif(alternatif koşul sağlanıyorsa): True dönüyorsa
    (burada yazılanı yap)
elif(alternatif koşul sağlanıyorsa): True dönüyorsa
    (burada yazılanı yap)
else:
    (burada yazılanı yap)
"""
"""
hava_durumu="yagısli"
if hava_durumu=="yagısli":
    print("şemsiyeni almalısın")
else:
    print("şemsiyeni alma")
#######################################################
hava_durumu="karli"
if hava_durumu=="yagısli":
    print("şemsiyeni almalısın")
elif hava_durumu=="karli":
    print("atkını almalısın")
elif hava_durumu=="günesli":
    print("tişörtünü giy")
elif hava_durumu=="firtina":
    print("dışarı çkmamalısın")
elif hava_durumu=="dolu":
    print("şemsiye almalısın")
else:
    print("sıkıntı yok")

yas=int(input("yaşınızı giriniz :"))
if(yas<18):
    print("bu mekana giremessiniz")
else:
    print("mekana hoşgeldiniz")
#########################################################
islem=int(input("1-4 arasında işlem seçiniz :"))

if (islem==1):
    print("1. işlem seçildi")
elif (islem==2):
    print("2.işlem seçildi")
elif (islem==3):
    print("3.işlem seçildi")
elif (islem==4):
    print("4.işlem seçildi")
else:
    print("geçersiz işlem")
"""
"""
note=float(input("notunuzu giriniz :"))
if (note>100):
    print("notun 100 den büyük olamaz geçersiz giriş")
elif (0>note):
    print("notun 0 dan küçük olamaz geçersin giriş")
elif (note>=90):
    print("notunuz : AA- dersten geçtiniz")
elif (note>=85):
    print("notunuz : AB- dersten geçtiniz")
elif (note>=80):
    print("notunuz : BB- dersten geçtiniz")
elif (note>=75):
    print("notunuz : BC- dersten geçtiniz")
elif (note>=70):
    print("notunuz : CC- dersten geçtiniz")
else:
    print("notunuz : CD- dersten kaldınız")
"""
"""
note=float(input("notunuzu giriniz :"))
if (note>100):
    print("notun 100 den büyük olamaz geçersiz giriş")
elif (0>note):
    print("notun 0 dan küçük olamaz geçersin giriş")
elif (note>=95) and (note<100):
    print("notunuz : dersten geçtiniz")
elif (note>=90) and (note<95):
    print("notunuz : AA- dersten geçtiniz")
elif (note>=85) and (note<90):
    print("notunuz : AB- dersten geçtiniz")
elif (note>=80) and (note<85):
    print("notunuz : BB- dersten geçtiniz")
elif (note>=75) and (note<80):
    print("notunuz : BC- dersten geçtiniz")
elif (note>=70) and (note<75):
    print("notunuz : CC- dersten geçtiniz")
else:
    print("notunuz : CD- dersten kaldınız")
"""















