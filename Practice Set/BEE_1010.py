# In this problem, the task is to read a code of a product 1,
# the number of units of product 1, the price for one unit of product 1,
# the code of a product 2, the number of units of product 2 and the price for
# one unit of product 2. After this, calculate and show the amount to be paid.
#
# Input
# The input file contains two lines of data. In each line there will be 3 values:
# two integers and a floating value with 2 digits after the decimal point.
#
# Output
# The output file must be a message like the following example where "Valor a pagar"
# means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must
# be presented with 2 digits after the point.
temp_variable = 0.0
for i in range(2):
    input_taker = input().split()
    code, unit, price = int(input_taker[0]), int(input_taker[1]), float(input_taker[2])
    temp_value = float(unit) * price
    total_value = temp_value + temp_variable
    temp_variable = total_value

print(f'VALOR A PAGAR: R$ {total_value:.2f}')



