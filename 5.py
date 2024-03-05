import turtle
turtule=turtle.Turtle()
x=int(input("enter your number:"))
color=input("enter the color of square:")
turtule.shape("turtle")
turtule.color(color)
for i in range(4):
    turtule.forward(x)
    turtule.right(90)
turtle.mainloop()