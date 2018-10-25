#-----------------------------------------------------------------------
# File------------project7.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #7
# Due-------------December 5th, 2017
#
# This program creates a computer game called Peeved Pigeons by using
# a distance formula with nummbers that the user inputs.
#------------------------------------------------------------------------
distance = float(input("Distance to pig (feet) -------- "))
print()

while True:
    
 
    angle = float(input("Angle of elevation (degrees) -- "))
    draw_length = float(input("Draw length (inches) ---------- "))
    print()

    if angle < 0 or angle > 90:
        print("Invalid input")
        break
    if draw_length < 0:
        print("Invalid input")
        break
    
    velocity = draw_length * 10
    velocity_function = velocity * velocity
    radians_angle = angle * 3.14159/180 
    import math
    sin_function = math.sin(2 * radians_angle)
    
    shot_distance = velocity_function * sin_function / 32.2

    minus = distance - shot_distance
    compare = abs(minus)
    compare = int(compare)
    off_distance = abs(compare - 2)

    if compare <= 2:
        print("OINK!!")
        break
    elif minus < 0:
        print("Result of shot ---------------- " + str(off_distance) + " feet too long")
    else:
        print("Result of shot ---------------- " + str(off_distance) + " feet too short")
    print()
    



