from turtle import forward, left, right, penup, pendown, exitonclick
    
n = int(input("Zadej kolik to ma mit uhlu: "))
strana = 40
uhel = 180 - (180 * (1 - 2 / n))

for i in range(n):
    forward(strana)
    left(uhel)

exitonclick()
