# kullanıcıdan veri alma - input() fonkisyonu
"""
input("bir sayı giriniz :")
a=input("bir sayı giriniz 2 :")
print(a)
print(" Sizin girdiğiniz sayı", a)

message=input("bana bir şey söyleyin size tekrar edeyim : ")
print(message)

girdi=input(" bir sayı giriniz : ")
print(girdi)

girdi=input(" bir sayı giriniz 2 : ")
print(type(girdi))

girdi=input(" bir sayı giriniz 3 : ")
print(type(int(girdi)))
print(type(str(int(girdi))))
"""

# PYTHON TEST OYUNU
"""Python da basit bir metin tabanlı youn yazıyoruz.
kendiniz yada arkadaşlarınızla oynayabilirsiniz.

"""
print("*** python testine hos geldiniz ***")
answer= input("testi çalıştırmaya hazır mısınız ? (evet/hayır) : ")
score=0
total_questions=3


# Evet-eVet-EVET-evet - kullanıcı bu değerlerin hepsini girebilir.
# lower() methodu - kullanıcının tüm karakterleri küçük olan bir dize döndürmesini sağlar
# upper() methodu - kullanıcının tüm karakterleri büyük olan bir dize döndürmesini sağlar
if answer.lower()=='evet':
    answer=input("Soru 1: Favori Pogramla Diliniz Nedir ? :")
    if answer.lower()=='python':
        score+=1
        print('doğru')
    else:
        print('Yanlış cevap')

    answer=input("Soru 2: Pythonda herhangi bir yazarı takip ediyormusunuz ? :")
    if answer.lower()=='evet':
        score+=1
        print('doğru')
    else:
        print('Yanlış cevap')

    answer=input("Soru 3: python öğrenmek için favori siteniz nedir ? :")
    if answer.lower() == 'python.org':
        score+=1
        print('doğru')
    else:
        print('Yanlış cevap')

puan=(score/total_questions)*100

print("Bu küçük bilgi yarışmasını oynadığınız için teşekkür ederiz")
print("Puanınız:", puan," - ",score,"Soru doğru!")
print("tekrar görüşmek üzere hoşçakalın")







