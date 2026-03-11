import turtle
import math

# --- Configuration ---
turtle.bgcolor("black")  # Set background to black
t = turtle.Turtle()
t.speed(0)              # 0 is the fastest animation speed
t.width(2)              # Set the thickness of the line

# List of colors to cycle through
colors = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

# --- The Drawing Loop ---
# This loop runs 360 times (a full circle)
for x in range(360):
    # Set the color based on the current loop number
    t.pencolor(colors[x % 7]) # The modulo % operator cycles through colors
    
    # Calculate a unique forward distance based on the loop index (x).
    # This creates the spiral effect.
    distance = x * 2.5 
    t.forward(distance)
    
    # The magic number: turning slightly MORE than 90 degrees
    # creates the complex, intersecting pattern.
    t.right(91) 

# --- Complete ---
# Keep the window open until you click on it
t.hideturtle() # Hide the turtle symbol when finished
turtle.exitonclick()
print("thank you")