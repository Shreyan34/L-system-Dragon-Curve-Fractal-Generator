# GENERATION OF L-SYSTEM DRAGON CURVE FRACTALS
# CREATED BY SHREYAN KUMAR MISHRA, SEPTEMBER 2025

import turtle as t # import dependencies
import time 

ANGLE = 90 # define the angle
LINE_HEIGHT = 2 # define the line height
ITERATIONS = 1 # initialize the variable that keeps track of iterations from 2
MAX_ITERATIONS = 15 # define the maximum iteration 
BACKGROUND = t.Screen().bgcolor('black') # get the background, and set it to black


# a simple function that reverses a string and returns the reversed string
def reverse(string):
    reversed_string = string[::-1]
    return reversed_string

# a function that traverses through a string and converts L --> R and R --> L
def parse(string):
    parseString = ""
    for i in range(len(string)):
        if string[i] == "L":
            parseString += "R"
        else:
            parseString += "L"
    return parseString

# a function that draws according to the rule. If L, then move forward and turn LEFT. For R, move forward and turn RIGHT
def draw(string):
    t.penup() # the following commands position the turtle at the right place in the screen
    t.goto(-300, 100)
    t.pendown()
    t.speed(0)
    t.color(['white']) # change the turtle pen colour to white
    for i in range(len(string)):
        if string[i] == "L":
            t.forward(LINE_HEIGHT)
            t.left(ANGLE)
        else:
            t.forward(LINE_HEIGHT)
            t.right(ANGLE)
            
t.title("Dragon Curve Fractals") # create the title

rule = "L" # start with an initial rule

while(ITERATIONS<=MAX_ITERATIONS):
    # start the main loop
    rev = reverse(rule) # first find the reverse of the rule
    par = parse(rev) # parse the rev rule
    result = rule + "L" + par  # find the result
    rule = result # update rule to result
    ITERATIONS += 1  # increment the iteration

start = time.perf_counter()
draw(result) # draw the result
t.hideturtle() # hide the turtle after drawing
print("Done!") # print a message on completion of the program
end = time.perf_counter() # calculate the time elapsed to complete the program
seconds_elapsed = end - start 
minutes_elapsed = seconds_elapsed / 60
print(f"Time taken to draw the fractal: {minutes_elapsed} minutes") # display the time elapsed
t.done() # save the screen after ending the loop

