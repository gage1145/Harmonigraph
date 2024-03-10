

from tkinter import *
import random
import math
import turtle



pendulums = [True] + [random.randint(0, 1) for _ in range(2)]
freqs = [random.randint(0, 20) for _ in range(6)]
amps = [random.randint(0, 200) for _ in range(6)]
phases = [random.randint(1, 6) + random.random() for _ in range(6)]
color_direction = [random.randint(0, 1) for _ in range(3)]
colors = [random.randint(0, 255) for _ in range(3)]
direction = 1
cycles = 5000
alias = 200
pen_weight = 2
color_change = True
pen_change = False



def harmonograph(frequencies: list, 
                 amplitudes: list, 
                 phases: list, 
                 pends: list, 
                 color_direction: list, 
                 color: list = [255, 255, 255], 
                 color_change: bool = False, 
                 direction: int = 1, 
                 iterations: int = 5000,
                 alias: int = 30, 
                 pen_size: int = 1,
                 pen_change: bool = False):
        
    window = turtle.Screen()
    window.bgcolor("black")
    window.colormode(255)
    window.screensize(400, 400)
    
    tim = turtle.Turtle()
    
    tim.hideturtle()
    tim.color(color)
    tim.speed(0)
    tim.pensize(pen_size)
        
    def PendulumX(t):
        return sum(amplitudes[i] * math.sin(frequencies[i] * float(t / alias) + \
            phases[i]) * math.exp(-0.01 * float(t / alias)) if pends[i] \
                else 0 for i in range(3))

    def PendulumY(t):
        return sum(amplitudes[i] * math.sin(frequencies[i] * float(t / alias) + \
            phases[i]) * math.exp(-0.01 * float(t / alias)) if pends[i-3] \
                else 0 for i in range(3, 6))

    def change_color(rgb_values):
        x = 0
        for i in rgb_values:
            if i % 255:
                if color_direction[x]:
                    i += 1
                else:
                    i -= 1
            else:
                if color_direction[x]:
                    i -= 1
                else:
                    i += 1
                color_direction[x] = not color_direction[x]
            rgb_values[x] = i
            x += 1
        return rgb_values
    
    path = []
    for i in range(iterations)[::direction]:
        xy = (PendulumX(i), PendulumY(i))
        path.append(xy)

    if color_change:
        color_list = []
        for _ in range(iterations):
            color = change_color(color)
            color_list.append(color[:])

    tim.up()
    if direction == 1:
        tim.goto(PendulumX(0), PendulumY(0))
    else:
        tim.goto(PendulumX(iterations), PendulumY(iterations))
    tim.down()

    x = 0
    for i in path:
        if color_change:
            tim.color(color_list[x])
        tim.goto(i)
        if pen_change:
            tim.pensize(pen_size * (iterations - x) / iterations)
        x += 1
    
    window.mainloop()

harmonograph(freqs, amps, phases, pendulums, iterations=cycles, color=colors, color_direction=color_direction, color_change=color_change, direction=direction, alias=alias, pen_size=pen_weight, pen_change=pen_change)
