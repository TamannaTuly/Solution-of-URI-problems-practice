# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of the square that has side B.
# e) the area of the rectangle that has sides A and B.
#
# Input
# The input file contains three double values with one digit after the decimal point.
#
# Output
# The output file must contain 5 lines of data. Each line corresponds to one of the areas
# described above, always with a corresponding message (in Portuguese) and one space between
# the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
input_taker = input().split()
A, B, C = float(input_taker[0]),float(input_taker[1]),float(input_taker[2])

area_rectangled_triangle = (A *C)/2#the area of the rectangled triangle that has base A and height C
area_radius_circle = 3.14159*C*C #the area of the radius's circle C. (pi = 3.14159)
area_trapezium = ((A+B)/2)*C #the area of the trapezium which has A and B by base, and C by height
area_square = B*B #the area of the square that has side B
area_rectangle = A*B #the area of the rectangle that has sides A and B

print(f'TRIANGULO: {area_rectangled_triangle:.3f}')#12.7 10.4 15.2
print(f'CIRCULO: {area_radius_circle:.3f}')
print(f'TRAPEZIO: {area_trapezium:.3f}')
print(f'QUADRADO: {area_square:.3f}')
print(f'RETANGULO: {area_rectangle:.3f}')

