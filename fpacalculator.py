# Program to calculate the required flight path angle in aviation
# Matthew Dean 2018

import math

altinput = False
while not altinput:
    try:
        altitude = int(input("Please enter altitude in feet: "))
        if altitude > 0:
            altinput = True
        else:
            print("Please enter a positive number. ")
    except ValueError:
        print("Please enter an integer. ")


threshinput = False
while not threshinput:
    try:
        threshdist = int(input("Please enter distance from runway threshold in feet: "))
        if threshdist > 0:
            threshinput = True
        else:
            print("Please enter a positive number. ")
    except ValueError:
        print("Please enter an integer. ")


fpa = math.degrees(math.atan(altitude / threshdist))

print ("FPA:", format(fpa, '.2f'), "Degrees")

input ('Press any key to exit...')
