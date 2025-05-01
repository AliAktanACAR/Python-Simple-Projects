#python mantıksal veri tipi - karşılasştırma operatörleri

a=True
print(type(a))
b=False
print(a)
print(b)
c='True'
print(type(c)) # <clas'str'
yas1=20
yas2=18
print(yas2>18) #False
# print(18>18)
print(yas2==18) #True
#print(18==18)
print(yas2!=18) #False # (!=) not
print( not yas2==18)
print(not yas2>18)
print(10>9)
print(10==9)
print(10<9)


a=200
b=33
if b>a:
    print("b a'dan büyüktür")
else:
    print("b a'dan büyük değildir")

print(bool("hello")) #true
print(bool(15)) #true

x="hello"
y=15
print(bool(x)) #true
print(bool(y)) #true

var1=0
var2=1
var3=9.7
print(bool(var1)) #false
print(bool(var2)) #true
print(bool(var3)) #true

