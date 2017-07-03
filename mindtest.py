import turtle

def draw_circle():
    swati = turtle.Turtle()
    swati.circle(100)
    swati.shape("arrow")
    swati.color("pink")
    
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    daksh = turtle.Turtle()
    daksh.shape("turtle")
    daksh.color("yellow","blue")
    daksh.speed(25)
    
    x=1
    while(x<=40):
        num=1
        while(num<=4):
            daksh.forward(100)
            daksh.right(90)
            num = num +1
        daksh.right(10)
        x = x+1
    daksh.left(310)
    daksh.forward(300)
    window.exitonclick()

draw_square()


