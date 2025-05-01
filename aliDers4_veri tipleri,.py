# Python da veri türleri

###################################################################################################
###    Tip      ###    Kısaltma   ###          örnek          ###
###    intiger  ###      int      ###          3, 10          ###
###    float    ###      float    ###        1.5, 8.0         ###
###    complex  ###     comp     ###           3j            ###
###    string   ###      str      ###    'S3m', '5', 'selam   ### ımmutable (değiştirilemez)
###    boolean  ###      bool     ###        True,False       ### mantıklı ifade
###    list     ###      list     ### [1,2.0,True, 'a', '1']  ### mutable (değiştirelebilir)
###    set      ###      set      ###    {1,2,true,'a'}       ### mutable
###    tuple    ###      tup      ###      (1,2,true)         ### immutable
### dictionary  ###      dict     ### {"İsim":"Ali","yas":12} ###
#                                 ##{key(anahtar): value(değer)}#
###################################################################################################

"""
# Örnekler
#
x='merhaba dünya' #str
print(type(x))
x=20   # int
print(type(x))
x=30.6 #float
print(type(x))
x=1j   #comp
print(type(x))
x=["elma","armut","üzüm"]  #list
print(type(x))
x={"elma","mandalina"}     #set
print(type(x))
x=((("elma","mandalina")))   #tup
print(type(x))
x={" isim:","ali","yas","12"} #dict
print(type(x))
x=True # bool
#
print(type(x))

# veri tiplerini belirtrek değişken oluşturma
a=5
b='5'
print(type(a))
print(type(b))

a=float(a)
print(a)
print(type(a))

a=str(a)
print(a)
print(type(a))

thisdict={
    "şasi": "ford",
    "model": "Mustang",
    "yaş":1964,
}
print(thisdict)
print(type(thisdict))
"""
# MATEMATİK OPERATÖRLERİ
# toplama işlemi
a=14
b=8
c=a+b
print(a+b)
print(c)

d=24
e=78
f=96
g=(d+e+f)
print(d+e+f)
print(g)

i=3.1
k=4.8
print(i+k)

j=8-5 #3
l=12-4 #8
print(j+l)

# çıkarma işlemi

a=8
b=3
print(a-b)
print(b-a)
c=a-b
print(c)

d=3.14
e=2.3
f=d-e
print(f)

# çarpma işlemi

a=10
b=32
print(a*b)
c=a*b
print(c)

c=3.1
d=4.3
e=c*d
print(e)

# bölme işlemleri

a=36
b=12
print(a/b)

c=3.6
d=4.2
e=c/d
print(e)