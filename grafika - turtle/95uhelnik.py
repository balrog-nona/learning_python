from turtle import forward, left, right, penup, pendown, exitonclick
    
strana = 15
uhel = 180 - (180 * (1 - 2 / 95))

for i in range(95):
    forward(strana)
    left(uhel)

exitonclick()
