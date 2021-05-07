'''
    Compute Screen Dimention ( Width and Height)
    This script computes screen dimention given its  screen size ( diagonal length ) and aspect ratio.


    Author  : Viki (a) Vignesh Natarajan
    Contact : vikiworks.io
'''

import sys
import math

def calculate_screen_width(d, ax, ay):
    s_width = ax * math.sqrt((d*d)/((ax*ax) + (ay*ay)))
    return s_width

def calculate_screen_height(d, ax, ay):
    s_height = ay * math.sqrt((d*d)/((ax*ax) + (ay*ay)))
    return s_height

diagonal_length=""
ax=""
ay=""
argc=len(sys.argv)
print("")

if argc < 4:
    #print("usage: ppi_calculator.py <screen diagonal length in inches> < screen resolution x > < screen resolution y >")
    print("\n\nFEED YOUR DISPLAY DETAILS:\n")
    inp = input("\tEnter the screen size ( in inches ) \t: ")
    diagonal_length=float(inp)
    inp = input("\tEnter the aspect ratio ( x-axis ) \t: ")
    ax=float(inp)
    inp = input("\tEnter the aspect ratio ( y-axis ) \t: ")
    ay=float(inp)
else:
    diagonal_length=float(sys.argv[1])
    ax=float(sys.argv[2])
    ay=float(sys.argv[3])

print("\n\nINPUTS:\n\n")

print("\tDiagonal Length ( Inches ) \t\t: ", diagonal_length)
print("\tAspect Ratio ( x ) \t\t\t: ", ax)
print("\tAspect Ratio ( y ) \t\t\t: ", ay)

s_width=calculate_screen_width(diagonal_length, ax, ay)
s_height=calculate_screen_height(diagonal_length, ax, ay)
print("\n\nRESULT ( inche ):\n\n")
print("\tScreen Width ( inches ) \t\t: ", s_width)
print("\tScreen Height ( inches ) \t\t: ", s_height)
print("\n\nRESULT ( cm ):\n\n")
print("\tScreen Width ( cm ) \t\t\t: ", (s_width*2.54))
print("\tScreen Height ( cm ) \t\t\t: ", (s_height*2.54))
print("")

