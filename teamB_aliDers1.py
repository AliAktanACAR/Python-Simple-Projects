# problem1: kullanıcıdan aldığınız 3 sayıyı çarparak ekrana yazdırın. Yazdırmayı format() methoduyla yapınız
"""
sayi1=int(input("Çarpmak istediğiniz 1. sayıyı giriniz:"))
sayi2=int(input("Çarpmak istediğiniz 2. sayıyı giriniz:"))
sayi3=int(input("Çarpmak istediğiniz 3. sayıyı giriniz:"))

print(format(sayi1*sayi2*sayi3))

sayiA=int(input("Çarpmak istediğiniz 1. sayıyı giriniz:"))
sayiB=int(input("Çarpmak istediğiniz 2. sayıyı giriniz:"))
sayiC=int(input("Çarpmak istediğiniz 3. sayıyı giriniz:"))
çarpim =sayiC*sayiB*sayiA

print("{}*{}*{}={} dir".format(sayiC,sayiB,sayiA,çarpim))

# problem2: kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle endeksini bulun.(kilo/boy(m)*boy(m)

boy=float(input("Boy:"))
kutle=int(input("Kütle:"))
carpim=(kutle/(boy*boy))
print("beden kitle endeksiniz : " , carpim)
"""
# problem3: bir aracın kilometrede ne kadar yaktığını ve kaç kilometre yol yaptığını alın ve sürücü toplam ne kadar ödemesi gerektiğini hesaplayın.
# benzin in 1 litresi 50 tl
yapilan_yol=int(input("yapılan_yol :"))
harcanan_benzin=int(input("harcanan_benzin: "))
ödeme=(harcanan_benzin*50)
print("1 kilometrede yakılan benzin" ,yapilan_yol/harcanan_benzin, ödeme)








