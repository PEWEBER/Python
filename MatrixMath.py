#---------------------------------------------------
# Paige Weber, L22812475
# Dr. Crawley, Computer Graphics
# 9/13/19
#---------------------------------------------------
# The user is prompted to select translation,
# rotation or scaling. With matrix multiplication,
# the program performs the request on a point
# provided by  user and returns the new point.
#---------------------------------------------------
import math

def translation (B, e, f):
    # set translation matrix
    A = [[1, 0, e],
         [0, 1, f],
         [0, 0, 1]]
    multiplication(A, B)

def rotation (B, d):
    # transalate the value given by the user (degrees) into radians
    d = d * (math.pi/180)
    # set rotation matrix
    A = [[math.cos(d), -1*math.sin(d), 0],
         [math.sin(d), math.cos(d), 0],
         [0, 0, 1]]
    multiplication(A, B)

def scaling (B, a, b):
    # set scaling matrix
    A = [[a, 0, 0],
         [0, b, 0],
         [0, 0, 1]]
    multiplication(A, B)

def multiplication(A, B):
    # multiply user matrix by the translation, rotation, or scaling matrix
    C = [[A[0][0] * B[0][0] + A[0][1] * B[1][0] + A[0][2] * B[2][0]],
         [A[1][0] * B[0][0] + A[1][1] * B[1][0] + A[1][2] * B[2][0]],
         [A[2][0] * B[0][0] + A[2][1] * B[1][0] + A[2][2] * B[2][0]]]
    # format the floats to only print out two decimal places
    # C[0][0] and C[1][0] are only printed because C[2][0] is a placeholder for multiplication
    print1 = float("{0:.2f}".format(C[0][0]))
    print2 = float("{0:.2f}".format(C[1][0]))
    # print out final answer in an intuitive format
    print("(" + str(print1) + ", " + str(print2) + ")")
   
    
# prompt user for type of calculation
print("1. Translation")
print("2. Rotation")
print("3. Scaling")
functionNum = input("Choose and option. Type '1', '2', or '3': ")

xVal = float(input("Enter the x coordinate: "))
yVal = float(input("Enter the y coordinate: "))

# put info given by user into a matrix
userPoint = [[xVal], [yVal], [1]]

# ask for info specific to the type of calculation and pass to function
if(functionNum == 1):  
    tranValX = float(input("Enter the translation value for the x coordinate: "))
    tranValY = float(input("Enter the translation value for the y coordinate: "))
    translation(userPoint, tranValX, tranValY)

elif(functionNum == 2):
    rotVal = float(input("Enter the rotation value for the coordinates (degrees): "))
    rotation(userPoint, rotVal)

else:
    scalValX = float(input("Enter the scaling value for the x coordinate: "))
    scalValY = float(input("Enter the scaling value for the y coordinate: "))
    scaling(userPoint, scalValX, scalValY)

