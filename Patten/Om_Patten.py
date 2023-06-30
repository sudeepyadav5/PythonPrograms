"""def print_om_pattern():
    om_pattern = [
        "        ॐॐॐॐॐॐ        ",
        "      ॐ      ॐ      ",
        "    ॐ          ॐ    ",
        "  ॐ              ॐ  ",
        " ॐ                ॐ ",
        "ॐ                  ॐ",
        " ॐ                ॐ ",
        "  ॐ              ॐ  ",
        "    ॐ          ॐ    ",
        "      ॐ      ॐ      ",
        "        ॐॐॐॐॐॐ        "
    ]

    for line in om_pattern:
        print(line)

# Call the function to print the Om pattern
print_om_pattern()"""

from turtle import *

s = Screen()
s.screensize(700, 1000)
speed(5)


def myPosition(x, y):
    penup()
    goto(x, y)
    pendown()


pensize(2)


def uuu():
    fillcolor('#ff641a')
    begin_fill()
    right(-40)
    circle(-100, 40)
    circle(-50, 50)
    left(2)
    circle(-80, 100)

    left(130)
    forward(40)
    right(-30)
    circle(60, 50)
    forward(60)
    circle(-40, 40)
    right(20)
    circle(-60, 80)
    right(-10)
    circle(-160, 30)
    right(-10)
    circle(-160, 30)
    circle(-100, 20)
    circle(-100, 20)
    right(10)
    circle(-100, 40)
    right(10)
    circle(-100, 40)
    right(10)
    circle(-100, 20)

    right(140)
    circle(100, 10)
    right(-15)
    circle(100, 20)
    right(-15)
    circle(100, 60)
    right(-5)
    circle(100, 30)
    right(-5)
    circle(20, 60)
    right(-5)
    circle(30, 80)
    left(-15)
    forward(40)
    left(10)
    circle(-40, 40)
    left(5)
    circle(-40, 40)

    right(-10)
    forward(10)
    left(-5)
    circle(-100, 20)

    left(140)
    circle(-130, 20)
    left(10)
    forward(20)
    left(-15)
    forward(20)
    left(15)
    circle(-130, 50)
    right(10)
    circle(-120, 120)
    left(10)
    circle(-120, 15)
    right(-15)
    forward(40)
    circle(120, 40)
    right(160)
    circle(-120, 40)
    forward(40)
    right(15)
    circle(120, 50)
    circle(70, 50)
    left(10)
    circle(80, 50)
    left(10)
    circle(30, 80)
    circle(60, 30)
    right(150)
    circle(150, 40)
    right(180)
    circle(120, 10)
    left(10)
    circle(30, 100)

    circle(60, 60)
    circle(20, 100)
    right(20)
    forward(2)
    circle(80, 60)

    right(175)
    circle(100, 40)

    end_fill()


def chandra():
    myPosition(70, 50)
    pensize(2)
    fillcolor('#ff641a')
    begin_fill()
    right(145)
    circle(180, 80)
    right(-30)
    # forward(2)
    circle(35, 70)
    right(-60)
    circle(35, 24)
    circle(-180, 71)

    end_fill()


def bindu():
    myPosition(180, 100)
    pensize(2)
    fillcolor('#ff641a')
    begin_fill()
    right(180)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    end_fill()


def shadeBindu():
    fillcolor('#bcbec5')
    begin_fill()
    left(120)
    forward(16)
    left(60)
    forward(40)
    left(120)

    forward(16)
    left(60)
    forward(40)
    end_fill()
    #    left(120)
    #    forward(16)

    myPosition(143, 67)
    fillcolor('#8f8888')
    begin_fill()
    right(90)
    forward(40)
    right(-24)
    forward(16)
    right(-150)
    forward(40)
    end_fill()


def shadeChandra():
    fillcolor('#8f8888')
    begin_fill()
    myPosition(290, 77)
    # circle(2)
    left(45)
    forward(16)
    left(32)
    circle(-180, 62)
    left(177)
    circle(180, 68)
    end_fill()


def shadeUuu():
    fillcolor('#bcbec5')
    begin_fill()
    myPosition(0, 0)
    # circle(2)
    left(-160)
    forward(16)
    left(30)
    circle(-100, 32)
    left(140)
    forward(16)
    right(-51)
    circle(150, 24)
    end_fill()

    myPosition(50, -30)
    fillcolor('#8f8888')
    begin_fill()
    # circle(2)
    left(-80)
    circle(-20, 100)
    left(10)
    circle(-45, 100)
    left(160)
    circle(45, 30)
    left(15.5)
    circle(65, 60)
    circle(18, 100)
    end_fill()

    myPosition(18, -68)
    fillcolor('#bcbec5')
    # circle(2)
    begin_fill()
    left(20)
    forward(16)
    left(60)
    circle(-150, 37)
    left(115)
    forward(16)
    left(65)
    circle(150, 37)
    # circle(2)
    end_fill()

    myPosition(38, -168)
    fillcolor('#8f8888')
    begin_fill()
    right(170)
    circle(-80, 40)
    left(-10)
    circle(-60, 70)
    left(10)
    circle(-80, 40)
    left(10)
    forward(5)
    left(156)
    forward(5)
    left(10)
    circle(100, 65)
    left(10)
    circle(60, 85)
    left(5)
    circle(40, 28)
    end_fill()
    # circle(2)

    myPosition(-192, -94)
    fillcolor('#bcbec5')
    begin_fill()
    left(129)
    forward(16)
    left(50)
    circle(-120, 40)
    left(10)
    forward(30)
    left(157)
    circle(150, 50)
    end_fill()
    # circle(2)

    myPosition(95, -110)
    fillcolor('#8f8888')
    begin_fill()
    left(205)
    forward(20)
    left(20)
    circle(70, 60)
    left(193)
    circle(-70, 60)
    right(35)
    forward(35)
    end_fill()
    # circle(4)

    myPosition(220, -114)
    fillcolor('#8f8888')
    begin_fill()
    right(160)
    circle(-25, 120)
    left(10)
    circle(-80, 110)
    left(167)
    circle(80, 35)
    left(5)
    circle(80, 70)
    right(10)
    pensize(4)
    circle(90, 30)
    pensize(2)
    right(10)
    circle(22, 150)
    end_fill()
    # circle(6)

    myPosition(-220, -94)
    pensize(8)
    left(50)
    circle(300)


# temp()
uuu()
chandra()
bindu()
shadeBindu()
shadeChandra()
shadeUuu()
ht()
done()