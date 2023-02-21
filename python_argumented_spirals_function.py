import turtle

win = turtle.Screen()
win.setup(800,600)
win.title("different spirals")

#draw star
def draw_star(x, y, num_sides, color):
    t = turtle.Turtle()
    t.speed("fast")
    t.penup()
    t.pencolor(color)
    t.pensize(2)
    t.goto(x,y)
    t.pendown()
    for count in range(100):
        
        t.forward(count)
        t.right(360/num_sides +2)
        
    
draw_star(50,50,3, 'blue')
draw_star(-100,100,4, "red")
draw_star(-100,-100,5,"purple")
draw_star(200,-200,6,'orange')