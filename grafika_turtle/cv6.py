from turtle import forward, left, right, penup, pendown, exitonclick
    

for i in range(5, 9):
    strana = 200 / i
    uhel = 180 - (180 * (1 - 2 / i))
    for x in range(i):
        forward(strana)
        left(uhel)
    penup()
    forward(strana + 100)
    pendown()
    

exitonclick()
