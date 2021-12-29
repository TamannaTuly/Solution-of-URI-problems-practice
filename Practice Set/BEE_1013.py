# Make a program that reads 3 integer values and present the
# greatest one followed by the message "eh o maior". Use the following formula:
# Input
# The input file contains 3 integer values.
#
# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.


list =[]
input_taker = input().split()
a, b, c = int(input_taker[0]), int(input_taker[1]), int(input_taker[2])
list.insert(0,a)
list.insert(1,b)
list.insert(2,c)

max = max(list)
print(f'{max} eh o maior')