from turtle import Turtle

def draw_ears(radius):
  """
  Purpose:This function draws both ears of mickey in red with about a pixel overlapping the face.
  Arguments: Requires the radius of the face to be passed
  """
  color = 'red' 
  go_to_right_ear_start(radius)
  ear_radius = radius / 2 # halves the radius to meet criteria for project
  draw_circle(ear_radius, color)
  go_to_left_ear_start(radius)
  draw_circle(ear_radius, color)

def go_to_right_ear_start(radius):
  """
  Purpose: Moves the turtle to 130 degrees on the face of mickey and faces down
           to enable the circle to be drawn in the right direction
  Arguments:Needs the face radius to determine how far to move
  """
  turtle.penup()
  turtle.circle(radius, extent=130)
  turtle.right(180)
  turtle.pendown()

def go_to_left_ear_start(radius):
  """
  Purpose: Moves the turtle home, then moves to -130 degrees on mickeys face to draw a
           symetrical ear opposed to the right ear
  Arguments: needs the face radius to determine how far to move. 
  """
  turtle.penup()
  turtle.home()
  turtle.circle(radius, extent=-130)
  turtle.right(180)
  turtle.pendown()

def draw_face(radius):
  """
  Purpose: Draws the main face of Mickey in blue. The size of the face dictates the
           size of the rest of the components
  Arguments: Needs a radius to determine size. 
  """
  color = 'blue'
  turtle.begin_fill()
  draw_circle(radius, color)
  turtle.end_fill()
  
def go_to_eye_start(radius):
  """
  Purpose: Moves the turtle back to home and thenm moves it to the correct height
           and prepares to draw both eyes.
  Arguments: Needs the face radius to calculate height 
  """
  turtle.penup()
  turtle.home()
  turtle.left(90)
  turtle.forward(radius * 1.2)
  
def draw_left_eye(eye_radius, radius, color):
  """
  Purpose: Draws the left eye of Mickey
  Arguments: needs an eye radius for eye size, face radius to determine eye height and a color
  """
  go_to_eye_start(radius)
  turtle.left(90)
  turtle.forward(radius * .2)
  turtle.right(90)
  turtle.pendown()
  draw_circle(eye_radius, color)
  
def draw_right_eye(eye_radius, radius, color):
  """
  Purpose: Draws the right eye
  Arguments: needs an eye radius for eye size, face radius to determine eye height and a color
  """
  go_to_eye_start(radius)
  turtle.right(90)
  turtle.forward(radius * .2)
  turtle.right(90)
  turtle.pendown()
  draw_circle(eye_radius, color)
  turtle.penup()

def draw_eyes(radius):
  """
  Purpose: Draws both Eyes on Mickey
  Arguments: Needs a radius to pass into both eye functions
  """
  color = 'red'
  eye_radius = radius * .2
  draw_left_eye(eye_radius, radius, color)
  draw_right_eye(eye_radius, radius, color)

def draw_circle(radius, color):
  """
  Purpose: Draws a circle to the left of the cursor + radius
  Arguments: needs a radius and color 
  """
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()


"""
NOTE: Turtle draws circles to THE LEFT of the arrow/turtle PLUS it's radius. 
      It is important to keep this in mind when prototyping.
"""
#Declares a turtle object to the function
turtle = Turtle()
#adds the title to the top of the project
turtle.screen.title("Scott Somers - CISC_179 mickey.py submission")
#this radius dictates the size of the face, which is then used for ears and eyes
radius = 100
#sets line and turtle color to red to match example given
turtle.color('red')
draw_face(radius)
draw_ears(radius)
draw_eyes(radius)
#hides the turtle at the end for cleanliness
turtle.hideturtle()
#leaves the turtle on screen until a mouse click
turtle.screen.exitonclick()