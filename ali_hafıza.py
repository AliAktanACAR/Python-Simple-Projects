# hafıza, sayı çiftleri bulma oyunu
"""
1. kaç vuruşun gerçekleşeceğini sayın ve yazdırın.
2. döşeme sayını 4x4 ızgara şeklinde düşünüyoruz.
3. tüm kaoların ne zaman ortaya çıkacağını tespit ediyoruz.
4. tek haneli kutucuğu ortalayın
5. karoların yerine harfleri kullanın
"""

from random import*
from turtle import*
from freegames import path

car=path("car.gif")
tiles=list(range(32))*2
state={"mark":None}
hide=[True]*64

def square(x,y):
#  (x,y) de siyah çerçeveli beyaz kare çizin
    up()
    goto(x,y)
    down()
    color("black","white")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x,y):
    # (x,y) kordinatlarını karo dizinine dönüştürür
    return int((x+200)//50+((y+200)//50)*8)
def xy(count):
    # Karo sayısını (x,y) koordinatlarını dönüştürür
    return (count%8)*50-200,(count//8)*50-200

def tap(x,y):
    # Dokunmaya bağlı olarak işareti ve gizli döşemeleri güncelleyin
    spot=index(x,y)
    mark= state["mark"]
    if mark is None or mark==spot or tiles [mark]!=tiles[spot]:
        state['mark']=spot
    else:
        hide[spot]=False
        hide[mark]=False
        state['mark']=None

def draw():
    # Resim ve döşeme çizin
    clear()
    goto(0,0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x,y=xy(count)
            square(x,y)
    mark=state['mark']

    if mark is not None and hide[mark]:
        x,y=xy(mark)
        up()
        goto(x+2,y)
        color('black')
        write(tiles[mark],font=('Arial',30,'normal'))

    update()
    ontimer(draw,100)

shuffle(tiles)
setup(420,420,370,0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
