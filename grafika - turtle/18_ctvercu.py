from turtle import forward, left, right, exitonclick, penup, pendown

strana = 100
uhel = 90

for x in range(18):
    for i in range(4):
        forward(strana)
        left(uhel)
    left(380/18)

#stonek
right(110)
forward(400)
left(180)
penup()
forward(4)
pendown()




exitonclick()
