#import turtle and random library
import turtle
import random

# make two different turtle objects
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# tell screen to not show automatically
screen = t1.getscreen()
screen.setup(500,500)
screen.tracer(1)

def draw_circle(radius, x, y, direction, line_color, fill_color):
  '''this function is called to make a circle of a certain radius, line color, and fill color'''
  t2.pencolor(line_color)
  t2.fillcolor(fill_color)
  t2.begin_fill()
  t2.circle(radius)       # draws the circle with radius parameter
  t2.end_fill()

def draw_polygon_window(num_side, side_length, x, y, direction, line_color, fill_color):
  '''this function is called to draw a polygon, which is used as a window in the program'''
  t1.penup()
  t1.goto(x, y)
  t1.fillcolor(fill_color)
  t1.pendown()
  t1.begin_fill()
  for i in range (6):       # loops used to finish drawing a perfect polygon
    t1.forward(50)
    t1.right(60)
  t1.end_fill()

def draw_shape_triangle(x, y, direction, line_color, fill_color):
  '''this function is called to draw a triangle, which is used as a roof in the program'''
  t1.fillcolor(fill_color)
  t1.begin_fill()
  t1.left(30)
  t1.forward(250)
  t1.left(120)
  t1.forward(250)
  t1.left(120)
  t1.forward(250)
  t1.end_fill()

def draw_house(line_color, fill_color):
  '''this function is called to make the main object of the program, which is the house'''
  t1.penup()
  t1.goto(125, -125)        # goes to the best coordinate possible to start the creation fo the house
  t1.pendown()
  t1.fillcolor(fill_color)
  t1.begin_fill()
  for i in range (2):       # used to make the borders of the house
    t1.forward(150)
    t1.left(90)
    t1.forward(250)
    t1.left(90)
  t1.end_fill()
  t1.penup()
  t1.forward(150)
  t1.pendown()
  draw_shape_triangle(0, 0, 0, line_color, 'red')       # called to make the roof with the fill color red
  draw_polygon_window(6, 200, -25, 0, 0, line_color, 'lightblue')     # called to make the window with the fill color lightblue

def draw_rays(length, radius):
  '''this function is used to draw the rays of the sun'''
  for i in range(4):      # the function is repeated depending on the different pairs of rays
    t2.penup()
    t2.forward(radius)
    t2.pendown()
    t2.forward(length)
    t2.penup()
    t2.backward(length + radius)
    t2.left(90)


def draw_sun(line_color, fill_color):
  '''this function is called to make the sun'''
  t2.penup()
  t2.goto(125, 125)       # goes to chosen location for the sun to be placed
  t2.pendown()
  draw_circle(24, 0, 0, 0, line_color, fill_color)        # draw_circle function is called to make the main base of the sun with radius 24
  t2.left(90)
  t2.penup()
  t2.forward(24)        # positions the turtle cursor for the drawing of the rays
  t2.pendown()
  draw_rays(25, 24)       # draw_rays function is called to draw bigger rays
  t2.right(45)
  draw_rays(15, 24)       # draw_rays function is called to draw smaller rays 

def draw_grass(x, y, fill_color):
  '''this function is called to form small lumps of grass around the house's base'''
  t2.penup()
  t2.goto(x, y)       # goes to location that is assigned when the function is called
  t2.pencolor('black')
  t2.pendown()
  t2.fillcolor(fill_color)
  t2.begin_fill()
  t2.setheading(0)        # makes sure that the grass is pointing upwards
  t2.left(120)
  length = random.randint(20, 30)      # sets length to a random integer for a different sized piece of grass
  t2.forward(length)
  t2.right(170)
  t2.forward(length)
  for i in range(3):        # loop to draw the whole form of the grass
    t2.left(150)
    length = random.randint(20, 30)
    t2.forward(length)
    t2.right(170)
    t2.forward(length)
  t2.end_fill()

def draw_ground(fill_color):
  '''this function is called to draw the main portion of the ground with a big box'''
  t1.penup()
  t1.goto(-250, 0)        # goes to the edge of the screen to begin drawing the ground
  t1.pendown()
  t1.fillcolor(fill_color)
  t1.begin_fill()
  t1.forward(500)
  t1.right(90)
  t1.forward(250)
  t1.right(90)
  t1.forward(500)
  t1.right(90)
  t1.forward(250)
  t1.end_fill()

def write_title():
  '''this function is called to write the title and the creators name in the roof of the house'''
  t2.penup()
  t2.goto(0, 75)
  t2.fillcolor('white')       # makes the text white
  t2.pencolor('white')
  t2.pendown()
  t2.write('Home by: Mayur Patel', True, align='center', font=('Comic', 12, 'normal'))        # used to print the title and creators name on the screen with certian font, size, and style restrictions
  t2.penup()

def draw_background(x, y, direction, line_color, fill_color):
  '''this function is called to call the other functions in the code to make a background for the scene'''
  screen.bgcolor('lightblue')       # makes the background color lightblue

  draw_ground(fill_color)       # calls the draw_ground function to make the ground with its color parameter
  draw_sun('orange', 'yellow')        # calls the draw_sun function to make the sun with its color parameters
  for i in range (20):      # loop used to make certain amount of grass drawings in the scene
    x = random.randint(-225, 225)       # assigns a random location under the house in the form of a box
    y = random.randint(-225, -125)        
    draw_grass(x, y, 'green')       # calls draw_grass function to make one picture of the grass

def main():
  '''main function to make the whole code draw the scene'''
  draw_background(0, 0, 0 , 'black', 'green')       # draw_background function is called to make the back scene with its color parameters
  draw_house('black', 'tan')      # draw_house function is called to make the main object with its color parameters
  
  write_title()       # write_title function is called to print the title and name of the creator of the scene

  t1.hideturtle()       # hides the turtle so only the scene can be viewed
  t2.hideturtle()

main()        # main function is called to run the whole program and make the scene