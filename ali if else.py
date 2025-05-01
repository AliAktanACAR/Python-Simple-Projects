a=2
b=3
c=4
print(a+b+c)

a=2
if (a==2):
    print(True)
print("MERHABA")

"""
if(koşul) # if bloğu koşul sağlanınca çalışır.
    # if bloğu - girintiye dikkat et
    #yazılan işlemler çalışır.
    ...









"""

hava_durumu="yagısli"
if (hava_durumu=="yagısli"):
    print("şemsiyeni almalısın")
else:
    print("şemsiyeni alma")

hava_durumu="karlı"
if (hava_durumu=="yagısli"):
    print("şemsiyeni almalısın")
elif hava_durumu=="karlı":
    print("Atkını almalısın")
else:
    print("şemsiyeni alma")