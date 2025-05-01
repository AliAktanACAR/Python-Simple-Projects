
#range() fonksiyonu
#fonksiyonlar bizim verdiğimiz "range" isimli bir yapı oluşturur. bu yapı listelere benzer
#range() fonksiyonunun, başlangıç, bitiş ve opsiyonel olarak artırma alarak listelere benzeyen bir sıra dizisi oluşturur

range(0,20)
print(range(0,20))
# yazdırmak için başına * koymamız gerekir
print(*range(0,20))
print(range(10)) #range(0, 10)
print(range(0,10)) #range (0, 10)
print(*range(10))
print(type(range))

#range ve list birbirinden iki farklı tip. Ancak birbirine çevirilebilen bir yapı
#range in başına list yazarsak çevirebliriz

list(range(10))
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

liste=list(range(0,20)) #typecasting-tip zorlaması
print(liste) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#broadcasting, aritmatik işlemler sırasında dizelerin farklı şekillere nasıl sahip olduğunu açıklar
print(list(range(10)))
print([*range(10)])
print([*range(2,7,2)]) # ...,...,2 (2 şer atlar)

liste=[1,3,2,4,5]
print(type(liste))

# döngülerde kullanma
for sayi in range(0,10):
    print(sayi)

for sayi in range(10):
    if sayi==5:
        print(sayi)

for sayi in range(1,20):
    print(" * "*sayi)



#enumarate() argümanı iki bağımsız değişken alır
#iterable (yinelenebilir)
#start (isteğe bağlıdır)

harfler=["a","b","c","d","e"] #5 elemanı var
for harf in harfler:
    print(harf)

harfler=["a","b","c","d","e"] #5 elemanı var
for harf in enumerate (harfler):
    print(harf)

harfler=["a","b","c","d","e"] #5 elemanı var
for index, harf in enumerate(harfler):
    print(harf)

harfler=["a","b","c","d","e"] #5 elemanı var
for index,harf in enumerate (harfler):
    #print(harf)
    #print(index)
    print(index,harf)

harfler=["a","b","c","d","e"] #5 elemanı var
for index, harf in enumerate(harfler):
    print(index+1,harf)

harfler = ["a", "b", "c", "d", "e"]  # 5 elemanı var 6
for index, harf in enumerate(harfler):
    print("{}.harf:{}".format(index + 1, harf))

market=["ekmek","süt","tereyağ"]
enumerateGrocery=enumerate(market)
print(type(enumerateGrocery))

print(list(enumerateGrocery))

enumerateGrocery=enumerate(market,10)
print(type(enumerateGrocery))

for count,item in enumerate(market,99):
    print(count,item)

#zip
#zip iki birbirine eşit listenin birbirine eklenmesini sağlar.

ulkeler=['TR','FR','DE']
siralamalar=range(1,4) #1,2,3
for ulke in zip(ulkeler,siralamalar):
    print(ulke)

first_name=['Ali','Leyla','Çınar','Tuna','Erda','Defne','Deniz','Umut','Ada','Ege','Beren']
last_name=['Acar','İnanç','İşler','Pullu','Gür','Özcan','Nesimoğlu','İyidir','Bingöl','Kabalak','Kolbakır']
age=[11,13,33,71,2,20,38,34,24,35,38]
for name in zip(first_name,last_name,age):
    print(name)
#for first_name, last_name, age in zip(first_name,last_name,age):
#print(f"{first_name} {last_name} {age} yaşındadır")

full_name_list=[('Ali' , 'Acar' , 11),('Leyla' , 'İnanç' , 13),('Çınar' , 'İşler' , 33),('Tuna' , 'Pullu' , 71),('Erda' , 'Gür' , 2),('Defne' , 'Özcan' , 20),('Deniz' , 'Nesimoğlu' , 38),('Umut' , 'İyidir' , 34),('Ada' , 'Bingöl' , 24),('Ege' , 'Kabalak' , 35),('Beren' , 'Kolbakır' , 28)]
first_name,last_name,age= list(zip(*full_name_list))

print(f"first name:{first_name}\nlast_name:{last_name}\nage:{age}")



