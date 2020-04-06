# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:19:19 2020

@author: Lunxr
"""


import math as mt
import turtle
# creates turtle window
turtle.setup(width=1000,height=800) 
wn = turtle.Screen() 
wn.title("Pokeball")
wn.bgcolor("White") 
#wn.tracer(50)
pb = turtle.Turtle() 
pb.hideturtle()
pb.speed(0)
# some intialized variables
x = 0
y = 0
pi = mt.pi
c = 1
# for loop used to make a pokeball and then end once created
for c in range(1,5):
    if c == 1: # makes the top hemisphere red
        # for drawing
        pb.color("Red")
        pb.penup()
        pb.pensize(20)
        pb.pendown()
        # initial conds
        r = 215
        theta = 0
        dtheta = pi / 40
        i = 0
        # loops iterates over 2pi for 100 radii of 215 from 0 to 215
        while theta <= pi:
            if i <= 41:
                pb.setpos(0,0) # sends pen back to origin every i
                theta = i*dtheta
                x = r*mt.cos(theta)
                y = r*mt.sin(theta)
                i += 1
                if i == 41:
                    theta = 10
            pb.setpos(x,y) # this allows a solid line of the radius to be 
            # printed instead of just the outer points of the circle
    if c == 2: # makes the white button in center
        # used for outline on button
        pb.color("Black")
        pb.penup()
        pb.setpos(0,-55)
        pb.begin_fill()
        pb.circle(55)
        pb.end_fill()
        # used for white button
        pb.color("White")
        pb.penup()
        pb.setpos(0,-40)
        pb.begin_fill()
        pb.circle(40)
        pb.end_fill()
    if c == 3: # makes the circle in the button
        # new pen settings
        pb.color("Black")
        pb.pensize(3)
        pb.penup()
        pb.setpos(27,0)
        pb.pendown()
        # inital conds
        r = 27
        theta = 0
        dtheta = pi / 32
        i = 0
        # this makes the tiny circle acts the same as other outline circle
        while theta <= 2*pi:
            if i <= 65:
                theta = i*dtheta
                x = r*mt.cos(theta)
                y = r*mt.sin(theta)
                i += 1
                if i == 65:
                    theta = 10
                pb.setpos(x,y)
    if c == 4: # makes the right line then the outter circle
        pb.pensize(20)
        # makes the left line
        pb.penup()
        pb.setpos(-215,0)
        pb.pendown()
        pb.setpos(-50,0)
        # makes the right line
        pb.penup()
        pb.setpos(50,0)
        pb.pendown()
        pb.setpos(215,0)
        # initial conds for outer circle
        r = 220
        theta = 0
        dtheta = pi / 32
        i = 0
        # set pen to outter part of circle
        pb.penup()
        pb.pensize(10)
        pb.setpos(220,0)
        pb.pendown()
        # makes the outer circle
        while theta <= 2*pi:
            if i <= 65:
                theta = i*dtheta
                x = r*mt.cos(theta)
                y = r*mt.sin(theta)
                i += 1
                if i == 65:
                    theta = 10
                pb.setpos(x,y)
# a pokeball should have been made
turtle.exitonclick() # click the window to exit
