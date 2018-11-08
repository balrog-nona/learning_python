from turtle import forward, left, right, penup, pendown, exitonclick
    
strana = 0.7
uhel = 20

for i in range(300):
    forward(strana)
    left(uhel)
    strana += 0.1



exitonclick()
