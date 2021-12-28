# Read 2 variables, named A and B and make the sum of these two variables,
# assigning its result to the variable X. Print X as shown below. Print endline
# after the result otherwise you will get “Presentation Error”.
#
# Input
# The input file will contain 2 integer numbers.
#
# Output
# Print the letter X (uppercase) with a blank space before and after the equal signal followed by the value of X, according to the following example.
#
# Obs.: don't forget the endline after all.

# A = int(input())
# B = int(input())
#
# X = str(A+B)

# print("X = "+X+"\n")
# print(f"X = {X}\n")
# print("X"+" "+"="+" "+X+"\n")#new line is printed by default that's why no need to write \n

a=int(input())
b= int(input())
x=a+b
print("X = %i"% x)


