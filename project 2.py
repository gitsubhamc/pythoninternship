import turtle

window=turtle.Screen()
window.title("ping pong developed by subham chakraborty")
window.bgcolor("yellow")
window.setup(width=800,height=600)
window.tracer(0)

# score
score_a=0
score_b=0


# code for paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350,0)

# code for paddle b

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=2)
paddle_b.penup()
paddle_b.goto(350,0)

# code for ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("violet")
ball.penup()
ball.goto(0,0)
ball.dx=0.09
ball.dy=0.09

#code for pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align="center",font=(("courier",24,"normal")))


#functions for implementation

def paddleA_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddleA_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddleB_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddleB_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddleA_up,"w")
window.onkeypress(paddleA_down,"s")
window.onkeypress(paddleB_up,"o")
window.onkeypress(paddleB_down,"k")


# main code for the game

while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b), align="center", font=(("courier", 24, "normal")))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a, score_b), align="center", font=(("courier", 24, "normal")))

    #paddle and ball collision
    if (ball.xcor() >340 and ball.xcor()<350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <-340 and ball.xcor()<-350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(340)
        ball.dx *= -1