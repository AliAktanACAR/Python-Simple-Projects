# python da kontrol ifadeleri - break-continue-pass

"""
python da kontrol ifadeleri bir değere ve mantığa dayalı olarak programı yürütme sırasında kontrolü sağlar
pyton bize 3 türlü kontrol ifadesi sağlar:
devam etmek-kırmak-geçmek


"""
i=0
while (i<20):
    print(i)
    if i<10:
        break # i nin değeri 10 olunca koşul sağlanıyor ve break ifadesi ile karşılaştığı için döngü sona eriyor
    i+=1
liste=[1,2,3,4,5,6,7,8,9]
for i in liste:
    if i==5:
        break
    print(i)

# continue ifadesi
# program continue ifadesi ile karşılaştığında geri kalan işlemleri yapmadan döngünün başına döner
while True:
    a=(input()) # ekrana giriş yapmak gerekiyor
    if len(a)<5:
        print("yeniden deneyin")
        continue #döngünün başına götürür
    else:
        print("merhaba dünya")
        break








