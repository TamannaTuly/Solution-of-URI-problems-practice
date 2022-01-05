# Read a value of floating point with two decimal places. This represents a monetary value.
# After this, calculate the smallest possible number of notes and coins on which the value can be decomposed.
# The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.
#
# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).
#
# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
userInput = float(input())
note100 = 100
note50 = 50
note20 = 20
note10 = 10
note5 = 5
note2 = 2

note1 = 1
note050 = 0.50
note025 = 0.25
note010 = 0.10
note005 = 0.05
note001 = 0.01

realNumberINt = int(userInput)
realNumberfloat = userInput - float(realNumberINt)

if realNumberINt >= note100 :
    countNote100 = int(realNumberINt/ note100)
    realNumberINt = realNumberINt-(note100*countNote100)
    # print(countNote1)
else:
    countNote100 = 0
    # print(realNumber)
if realNumberINt >= note50:
    countNote50 = int(realNumberINt/ note50)
    realNumberINt = realNumberINt-(note50*countNote50)
    # print(countNote2)
    # print(realNumber)
else:
    countNote50 = 0

if realNumberINt >= note20:
    countNote20 = int(realNumberINt/ note20)
    realNumberINt = realNumberINt-(note20*countNote20)
    # print(countNote3)
    # print(realNumber)
else:
    countNote20 = 0

if realNumberINt >= note10:
    countNote10 = int(realNumberINt/ note10)
    realNumberINt = realNumberINt-(note10*countNote10)
    # print(countNote4)
    # print(realNumber)
else:
    countNote10 = 0

if realNumberINt >= note5:
    countNote5 = int(realNumberINt/ note5)
    realNumberINt = realNumberINt-(note5*countNote5)
    # print(countnote5)
    # print(realNumber)
else:
    countNote5 = 0

if realNumberINt >= note2:
    countNote2 = int(realNumberINt/ note2)
    realNumberINt = realNumberINt-(note2*countNote2)
    # print(countnote6)
    # print(realNumber)
else:
    countNote2 = 0

if realNumberINt >= note1:
    countNote1 = int(realNumberINt/ note1)
    realNumberINt = realNumberINt-(note1*countNote1)
    # print(countnote7)
    # print(realNumber)
else:
    countNote1 = 0

# realNumberfloat = userInput - float(realNumberINt)

print(f'{countNote100}\n{countNote50}\n{countNote20}\n{countNote10}\n{countNote5}\n{countNote2}\{countNote1}\n{realNumberfloat}')