# Read three values (variables A, B and C), which are the three
# student's grades. Then, calculate the average, considering that
# grade A has weight 2, grade B has weight 3 and the grade C has
# weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.
#
# Input
# The input file contains 3 values of floating points (double) with one digit after the decimal point.
#
# Output
# Print the message "MEDIA"(average in Portuguese) and the student's average according
# to the following example, with a blank space before and after the equal signal.

A = float("{:.1f}".format(float(input())))
B = float("{:.1f}".format(float(input())))
C = float("{:.1f}".format(float(input())))

A_default = float(2)
B_default = float(3)
C_default = float(5)

# print(type(A_default))
MEDIA = ((A*A_default)+(B*B_default)+(C*C_default))/(A_default+B_default+C_default)

print(f'MEDIA = {MEDIA:.1f}')#need to print using decimal point as this is the shown format but not the said one