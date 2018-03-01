# Program to calculate the required flight path angle in aviation
# Matthew Dean 2018

import math

altitude = int(input("Please enter altitude in feet: "))

threshdist = int(input("Please enter distance from runway threshold in feet: "))

fpa = math.degrees(math.atan(altitude / threshdist))

print ("FPA:", format(fpa, '.2f'), "Degrees")

input ('Press any key to exit...')
