# Pong Game !

import turtle
import winsound

ekran = turtle.Screen()
ekran.title('Pong by KasiaRLZ')
ekran.bgcolor('black')
ekran.setup(width=800, height=600)
ekran.tracer(0)

# Wynik
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)

# Piłka
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Funkcion 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Funkcja w dół
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Wiązanie z klawiaturą
ekran.listen()
ekran.onkeypress(paddle_a_up, 'w')
ekran.onkeypress(paddle_a_down, 's')
ekran.onkeypress(paddle_b_up, 'Up')
ekran.onkeypress(paddle_b_down, 'Down')

# Loopka do gry
while True:
    ekran.update()

    # Poruszanie piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Granice
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('pong/bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('pong/bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if paddle_a.ycor() > 260:
        paddle_a.sety(260)

    if paddle_a.ycor() < -260:
        paddle_a.sety(-260)

    if paddle_b.ycor() > 260:
        paddle_b.sety(260)

    if paddle_b.ycor() < -260:
        paddle_b.sety(-260)


    # Paddle i piłka 
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('pong/bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('pong/bounce.wav', winsound.SND_ASYNC)