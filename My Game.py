# My game
import turtle
import random
import pygame

wn = turtle.Screen()
wn.title("MY game")
wn.bgcolor("black")
wn.setup(width=900, height=400)
wn.tracer(0)

# Score
score = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=3, stretch_wid=1)
paddle.penup()
paddle.goto(0, -150)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 190)
ball.dy = -0.1
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 160)
pen.write("Player Score : 0", align="center", font=("Courier", 24, "bold"))


# Functions
def paddle_right():
    x = paddle.xcor()
    x += 40
    paddle.setx(x)
    if paddle.left <= 420:
	    paddle.left = 420


def paddle_left():
    x = paddle.xcor()
    x -= 40
    paddle.setx(x)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop

while True:
    wn.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)

    # Set ball back to random position
    a = random.randint(-420, 420)
    b = random.randint(180, 190)

    # Border checking
    if ball.ycor() < -190:
        ball.goto(a, b)
        score = 0 
        pen.clear()
        pen.write("Player Score : {} You Lost Your Progress".format(score), align="center", font=("Courier", 24, "bold"))

    # Paddle and ball collisions
    if paddle.distance(ball) < 20:
        ball.goto(a, b)
        score += 1
        pen.clear()
        pen.write("Player Score : {}".format(score), align="center", font=("Courier", 24, "bold"))
