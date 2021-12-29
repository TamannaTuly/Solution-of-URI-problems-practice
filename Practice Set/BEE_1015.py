# Read the four values corresponding to the x and y axes
# of two points in the plane, p1 (x1, y1) and p2 (x2, y2)
# and calculate the distance between them, showing four
# decimal places after the comma, according to the formula:
#
# Distance =
#
# Input
# The input file contains two lines of data. The first one
# contains two double values: x1 y1 and the second one also
# contains two double values with one digit after the decimal
# point: x2 y2.
#
# Output
# Calculate and print the distance value using the provided
# formula, with 4 digits after the decimal point.
import math
x0 =0.0
y0 =0.0
for i in range(2):
    input_taker = input().split()
    x, y = float(input_taker[0]),float(input_taker[1])
    distance1 =((x-x0)*(x-x0)) + ((y-y0)*(y-y0))
    x0 = x
    y0 = y
finalDistance = math.sqrt(distance1)
print(f'{finalDistance:.4f}')
