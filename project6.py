#--------------------------------------------------
# File-------------project6.py
# Developer--------Paige Weber
# Course-----------CS1213-03
# Project----------Project #6
# Due--------------November 16th, 2017
#
# This program computes an approximation of sin
# by prompting the user to input a value of x.
#---------------------------------------------------
def sin(a, b):
    top = a**b
    import math
    bottom = math.factorial(b)
    answer = top/bottom
    return answer
#---------------------------------------------------
while True:
    value = float(input("Enter a value for x ------------- "))
    newcount = 3
    answer = value
    for count in range(2, 21):
        sinVal = sin(value, newcount)
        add = ((-1)**(count + 1))
        newcount = newcount + 2
        answer = add * sinVal + answer
    print("The apporximation for sin is ---- %2.5f"%answer)
    reply = str(input("Would you like to do it again? -- "))
    if reply != "Yes":
        break
    
   

              


