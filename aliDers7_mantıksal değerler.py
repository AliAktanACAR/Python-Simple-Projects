# mantıksal değerler ve karşılaştırma operatörleri

#karşılaştırma operatörleri
"""
operatör    ne demek?     görevi
 ==     eşşitir       iki değer birbirine eşitse True,değilse False
 !=    eşit değil      iki değer birbirine eşit değilse True, eşitse False
  >      küçüktür      saldaki değer sağdaki değerden büyükse True,değilse false
  <      büyüktür      saldaki değer sağdaki değerden küçükse True,değilse false
  <=  küçük veya eşit  soldaki değer sağdaki değerden küçük veya eşitse True,değilse false
  >=  büyük veya eşit  soldaki değer sağdaki değerden büyük veya eşitse True,değilse false
"""
print("mehmet"=="mehmet") #true
print("mehmet"=="ali") #false
print("mehmet"!="ali") #true
print("umut"<"defne") #false
print( 98>45 ) #true
print( 2<3 ) #true
print( 2>3 ) #false
print(54>=54) #true
print(35<=45) #true

#değişkenler ile uygulama
x=5
y=8
print("x==y", x==y) #false
print("x!=y", x!=y) #true
print("x>y", x>y) #false
print("x<y", x<y) #true
print("x>=y",x>=y) #false
print("x<=y", x<=y) #true

# mantıksal operatörler And-Or-Not(değerleri karşılaştırmak için üç mantıksal operatör vardır.)
"""
boolen     ne demek?                        örnek
and      ikiside doğruysa true            x and y
or       en az birisi doğruysa true       x  or y
not      yanlızca yanlışsa True             not x
"""
print(9>7and(2<4)) #true true------> true
print(8==8)or(6!=6) #true false------> true
print(not(3<1)) #True
print(-0.2>1.4)and(0.8<3.1) #false true------> false
print(7.5==8.9)or(9.2!=9.2) #false false-----> false
print(not(-5.7<=0.3)) #false

#doğruluk tablosu
"""
    == doğruluk tablosu
    x==y         dönüştipi
    true==true     true
    true==false    false
    false==true    false
    falsee==false   true
    
    and doğruluk tablosu
    x and y         dönüş tipi
    true and true      true
    true and false     false
    false and true     false
    false ans false    false
    
    or doğruluk tablosu
        x or y     dönüş tipi
    true and true      true
    true and false     true
    false and true     true
    false ans false    false
    
    not doğruluk tablosu
    not x        donüş tipi
    not true        false
    not false       true
"""
print(1<2 and "erda"=="erda") #true
print(3<2 and "erda"=="erda") #false

a=0
b=2
c=3
if a>b and b<c:
    print(True)
else:
    print(False)

if a and b and c: #false true true------>false
    print("tüm değerler True boolen değere sahiptir")
else:
    print("en az bir sayı False boolean değere sahiptir")
print(bool(a))
print(bool(b))
print(bool(c))

a=1
b=2
c=4

if a>b or b<c: #false true------> true
    print(True)
else:
    print(False)

a=10
b=1

if a==0:
    print(True)
if (a==b):
    print(True)
if a!=b:
    print(True)






