#pong
import turtle
import winsound
wn = turtle.Screen()
wn.title("Manas")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid= 5,stretch_len=1)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid= 5,stretch_len=1)



ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1
score_a = 0
score_b = 0
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B : 0", align = "center", font = ("Courier",24,"normal"))
def check_winner():
    if score_a == 10:
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player A Wins!", align="center", font=("Courier", 36, "bold"))
        return True
    elif score_b == 10:
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player B Wins!", align="center", font=("Courier", 36, "bold"))
        return True
    return False
#movements

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
# main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    ## border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1 
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a,score_b), align = "center", font = ("Courier",24,"normal"))
        check_winner();
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a,score_b), align = "center", font = ("Courier",24,"normal"))
        check_winner();
    ##paddle and ball collisions
    if (ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor() +40) and (ball.ycor() > paddle_b.ycor() - 40 )and (ball.xcor() < 350):
        ball.dx *= -1
        ball.setx(340)
    if (ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() +40) and (ball.ycor() > paddle_a.ycor() - 40 )and (ball.xcor() > -350):
        ball.dx *= -1
        ball.setx(-340)
    
