import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
  tim.forward(10)

def move_backward():
  tim.backward(10)

def turn_left():
  tim.left(10)

def turn_right():
  tim.right(10)

def wipe():
  tim.clear()
  tim.reset()

screen.listen()
screen.onkey(fun=move_forward , key='w')
screen.onkey(fun=move_backward , key='s')
screen.onkey(fun=turn_left , key='a')
screen.onkey(fun=turn_right , key='d')
screen.onkey(fun=wipe , key='space')
screen.exitonclick()