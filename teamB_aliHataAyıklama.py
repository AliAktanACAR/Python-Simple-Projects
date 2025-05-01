# Hata ayıklama
"""

try-catch-finally(dene-yakala-sonunda)
try blok: hata kontrol yapısının try bloğu basit olanıdır. bir hata çıkması beklenen koduişaretle.
Kendi başına bişey yapmaz daha çok bir işaretçidir.
bu nedenle bilgisayar hangi kodun hatalarının daha sonra ele alınıcağını bilir.
bilgisayar hata ortaya çıkana kadar try bloğundaki kodu çalıştıracak
bir hata oluşursa kod try bloğunın geri kalanına atlayacak ve bir sonraki catch bloğundaki koda atlayacaktır.

catch blok:bilgisayar bir try block ile karşılaştığında blok sırasında bir hata oluşursa catch bloğuna atlaması gerektiğine dair "zihinsel" bir not verir.
Catch bloğu try bloğunda beklenen bir hata ile karşılaştığında bilgisayarın çalıştırması gereken kodu içerir

Finally blok: son olarak bazı programlama dillerinde finally block bulunur.
Finally bloğu başarılı olsun yada olmasın,try bloktan sonra çalıştırılması gereken kodu içerir
Try bloğundaki kod hatasız çalışıyorsa try bloğunda tamamlandığında yürütme finally bloğuna atlayacak.
try bloğundaki kod hatayla karşılaştıysa yürütme bir sonraki catch bloğunda olanı çalıştırır ve ardından finally bloğundaki kodu çalıştırır

"""
#############################################
"""
myString = "bu bir dizi değildir."
print("my string i int sayısına dönüştür")
# print(int(myString))  ValueError: invalid literal for int() with base 10: 'bu bir dizi değildir.
myInt = int(myString)
print(myInt)
print("tamamlandı")
"""
#############################################
"""
myString =  "bu bir dizi değildir." #burası sadece string
mySayi = "10"
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print(myInt)
except:
    pass
print("tamamlandı")
"""
#############################################
"""
myString =  "bu bir dizi değildir." #burası sadece string
mySayi = "10"
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print(myInt)
except:
    print("myString bir tamsayıya dönüştürülemez")
print("Tamamlandı")
"""
#############################################
"""
myString =  "10"
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print("String#"+ 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
except:
    print("myString bir tamsayıya dönüştürülemez")
print("Tamamlandı")
"""
#############################################
"""
myString = "bu bir dizi değildir."
try :
    print("my string i int sayısına dönüştür")
    print("String#" + 1 + " : "  + myString)
    #TypeError: can only concatenate str (not "int") to str
    myInt = int(myString)
    print(myInt)
except ValueError as error:
    print("error")
    #print("myString bir tamsayıya dönüştürülemez")
print("Tamamlandı")
"""
#############################################
"""
myString = 10
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print("String#"+ 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
except ValueError as error:
    print("Error1")
except TypeError as error:
    print("Error2")
print("tamamlandı")
"""
#############################################
"""
myString = 10
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print("String#"+ 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
    print(1/0)
except ValueError as error:
    print("Error1")
except TypeError as error:
    print("Error2")
print("tamamlandı")
"""
#############################################
"""
myString = 10
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print("String#"+ 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
    print(1/0)
except (TypeError,ValueError) as error:
    print("TypeError ya da ValueError oluştu ")
except Exception as error:
    print("başka bir hata var")
#except TypeError as error:
    #print("Error2")
print("tamamlandı")
"""
#############################################
"""
myString = 10
try :
    print("my string i int sayısına dönüştür")
    print(1 / 0)
    myInt = int(myString)
    print("String#"+ 1 + " : " + myString)
    myInt = int(myString)
    print(myInt)
except (TypeError,ValueError) as error:
    print("TypeError ya da ValueError oluştu ")
except Exception as error:
    print("başka bir hata var")
#except TypeError as error:
    #print("Error2")
print("tamamlandı")
"""
"""
myString = 10
try :
    print("my string i int sayısına dönüştür")
    myInt = int(myString)
    print(myInt)
except (TypeError,ValueError) as error:
    print("TypeError ya da ValueError oluştu ")
except Exception as error:
    print("başka bir hata var")
else:
    print("tamamlandı")
print("tamamlandı_1")
"""

### Else dosya girişi

"""
try:
    inputFile=open("inputFile.txt", mode="r")
    for line in inputFile:
        print(line)
    inputFile.close()
except IOError as error:
    print("bir giriş hatası oluştu")
"""
#############################################
"""
try:
    inputFile=open("inputFile.txt", mode="r")
except IOError as error:
    print("bir giriş hatası oluştu")
else:
    for line in inputFile:
        print(line)
    inputFile.close()
"""

try:
    inputFile=open("FakeinputFile.txt", mode="r") #var olmayan bir dosya adı
except IOError as error:
    print("bir giriş hatası oluştu")
else:
    for line in inputFile:
        print(line)
    inputFile.close()




