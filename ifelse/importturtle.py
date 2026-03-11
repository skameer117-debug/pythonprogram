import turtle

# 1. Setup the screen and the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(3) # Set a moderate speed

# 2. Drawing Logic (The Square)
# We use a simple loop (repeat 4 times)
for _ in range(4):
    t.forward(100) # Move forward 100 pixels
    t.right(90)    # Turn right 90 degrees

# 3. Complete
turtle.done()