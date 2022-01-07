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
realNumberINt = int(userInput)
userInputF = userInput - float(realNumberINt)
finalFLoat = float(userInputF)
# finalFLoat = float("{:.2f}".format(userInputF))
# print(type(finalFLoat))
# print(finalFLoat)
# # print(type(userInputF))
# # print(userInputF)
note100 = 100
note50 = 50
note20 = 20
note10 = 10
note5 = 5
note2 = 2

note1 = 1.00
note050 = 0.50
note025 = 0.25
note010 = 0.10
note005 = 0.05
note001 = 0.01

# realNumberINt = int(userInput)
# realNumberfloat = userInput - float(realNumberINt)


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

finalFLoat = float(realNumberINt)+finalFLoat

if finalFLoat >= note1:
    countNote1 = int(finalFLoat/ note1)
    finalFLoat = finalFLoat-(note1*countNote1)
    # print(countnote7)
    # print(realNumber)
else:
    countNote1 = 0
# print(realNumberINt)
if finalFLoat >= note050:
    countNote050 = int(finalFLoat/ note050)
    finalFLoat = finalFLoat-(note050*countNote050)
    # print(countnote7)
    # print(realNumber)
else:
    countNote050 = 0

if finalFLoat >= note025:
    countNote025 = int(finalFLoat / note025)
    finalFLoat = finalFLoat - (note025 * countNote025)
else:
    countNote025 = 0

if finalFLoat >= note010:
    countNote010 = int(finalFLoat / note010)
    finalFLoat = finalFLoat - (note010 * countNote010)
else:
    countNote010 = 0

if finalFLoat >= note005:
    countNote005 = int(finalFLoat / note005)
    finalFLoat = finalFLoat - (note005 * countNote005)
else:
    countNote005 = 0

if finalFLoat >= note001:
    countNote001 = int(finalFLoat / note001)
    finalFLoat = finalFLoat - (note001 * countNote001)
else:
    countNote001 = 0

print(f'NOTAS:\n{countNote100} nota(s) de R$ 100.00\n{countNote50} nota(s) de R$ 50.00\n{countNote20} nota(s) de R$ 20.00\n{countNote10} nota(s) de R$ 10.00\n{countNote5} nota(s) de R$ 5.00\n{countNote2} nota(s) de R$ 2.00\nMOEDAS:\n{countNote1} moeda(s) de R$ 1.00\n{countNote050} moeda(s) de R$ 0.50\n{countNote025} moeda(s) de R$ 0.25\n{countNote010} moeda(s) de R$ 0.10\n{countNote005} moeda(s) de R$ 0.05\n{countNote001} moeda(s) de R$ 0.01')

# realNumberfloat = userInput - float(realNumberINt)

# print(f'{countNote100}\n{countNote50}\n{countNote20}\n{countNote10}\n{countNote5}\n{countNote2}\n{countNote1}\n')


