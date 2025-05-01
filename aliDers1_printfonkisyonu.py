# print fonkisyonu ve formatlama

print("Merhaba dünya")
print("Hello world")
print("ali çok yakışıklı")
print("kodlama öğrenmek çok eğlencelidir herkese tavsiye ederim")
print("özgür kazmanın en ağırı")
print('özgür kazmanın en ağırı')
print("""özgür kazmanın en ağırı""")

print("python dersleri")
print("python dersleri","python dersleri")



# \n = newline - bir satır aşşağı geçirir
print("python dersleri\npython dersleri")

print("ali\naktan\naçar\n")

#\t = tab - belli bir mesafe boşluk bırakır
print("ankaranın bağları")
print("ankaranın\t\tbağları\t\nbüklümbüklüm\tyolları")

# end parametresi
print("python dersleri",end="")
print("python dersleri")
print("python dersleri",end=" ")
print("python dersleri")
print("python dersleri",end=",")
print("python dersleri")
print("python dersleri",end="\n")
print("python dersleri")

# sep parametresi

print("www","team","3390")
print("www","team","3390",sep=".")

print("selam gençler")

# format

a=8
b=5
c=a+b
print(c)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("{}+{}'nın toplamı {} dır".format(a,b,a+b))
print("Benim Adım Ali")
print("Benim Adım {}".format("Ali"))
print("Benim Adım :{}, Yaşım : {}".format("Ali",12))
print("Benim Adım :{}, Yaşım : {}".format(18,"müfit"))

print("Benim Adım = {0}, Yaşım = {1}".format("Ali",12))
print("Benim Adım = {1}, Yaşım = {0}".format("Ali",12))
print("Benim Adım = {ad}, Yaşım = {yas}".format(ad="ali",yas=12))
print("Benim Adım = {yas}, Yaşım = {ad}".format(ad="ali",yas=12))
print("Yaşım = {yas}, Benim Adım = {ad}".format(ad="ali",yas=12))

