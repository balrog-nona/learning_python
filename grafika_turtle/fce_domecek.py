from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt

n = float(input("Zadej velikost domecku: "))
d = 70 * n
prepona_druhou = (d ** 2) + (d ** 2)
prepona = sqrt(prepona_druhou)

def domecek(velikost):
    for i in range(4):
        forward(d)
        left(90)
    left(45)
    forward(prepona)
    left(45 + 90)
    penup()
    forward(d)
    left(90 + 45)
    pendown()
    forward(prepona)
    left(45 + 90)
    penup()
    forward(d)
    pendown()
    left(45)
    forward(prepona / 2)
    left(90)
    forward(prepona / 2)


domecek(n)

exitonclick()
