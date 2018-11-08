from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt

for i in range(4):
    forward(100)
    left(90)

left(45)

prepona_druhou = (100 ** 2) + (100 ** 2)
prepona = sqrt(prepona_druhou)

forward(prepona)

left(45 + 90)
penup()
forward(100)
left(90 + 45)
pendown()
forward(prepona)
left(45 + 90)
penup()
forward(100)
pendown()
left(45)
forward(prepona / 2)
left(90)
forward(prepona / 2)


exitonclick()

