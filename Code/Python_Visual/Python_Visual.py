import turtle                   # For drawing
import serial                   # For get arduino data
from random import randint      # To get random colors

num_param = 3
list_param = [0]*num_param

ser = serial.Serial('/dev/ttyUSB0', 115200)

# Setup the screen with a title
screen = turtle.Screen()
screen.title('looping turtle')
screen.bgcolor("black")

# Setup the screen's borders
width, height = turtle.window_width(), turtle.window_height()
minX, maxX = -width/2, width/2
minY, maxY = -height/2, height/2

# Drawing parameters
screen.colormode(255)       # Use colormode 255, 255, 255
screen.tracer(100, 0)       # tracer(Frame_to_skip, Delay)

# Setup the RED pixel
red = turtle.Turtle()
red.hideturtle()
red.goto(0, 0)
red_size, red_speed, red_alpha = 10, 100, -1

# Setup the GREEN pixel
green = turtle.Turtle()
green.hideturtle()
green.goto(width/2, -height/2)
green_size, green_speed, green_alpha = 10, 100, 1

# Setup the BLUE pixel
blue = turtle.Turtle()
blue.hideturtle()
blue.goto(-width/2, height/2)
blue_size, blue_speed, blue_alpha = 10, 100, 1


# Red Pixel parameters
def red_p(speed, alpha, size):
    red.width(size)
    red.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

    red.forward(speed)
    if not minX <= red.xcor() <= maxX or not minY <= red.ycor() <= maxY:
        red.left(180 + alpha)


# Green Pixel parameters
def green_p(speed, alpha, size):
    green.width(size)
    green.pencolor(0, 1, 0)

    green.forward(speed)
    if not minX <= green.xcor() <= maxX or not minY <= green.ycor() <= maxY:
        green.left(180 + alpha)


# Blue Pixel parameters
def blue_p(speed, alpha, size):
    blue.width(size)
    blue.pencolor(0, 0, 1)

    blue.forward(speed)
    if not minX <= blue.xcor() <= maxX or not minY <= blue.ycor() <= maxY:
        blue.left(180 + alpha)


def get_param():
    msg = ser.readline(24).decode('ascii')
    cast_msg = int(msg)
    return cast_msg


def assign_param():
    for i in range(0, num_param):
        param = get_param()
        list_param[i] = param


while True:
    assign_param()
    red_speed = list_param[0]
    red_alpha = list_param[1]
    red_size = list_param[2]

    red_p(red_speed, red_alpha, red_size)
    '''
    green_p(green_speed, green_alpha, green_size)
    blue_p(blue_speed, blue_alpha, blue_size)
    '''
    screen.update()
