# In this problem you have to read an integer value and calculate the
# smallest possible number of banknotes in which the value may be decomposed.
# The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.
#
# Input
# The input file contains an integer value N (0 < N < 1000000).
#
# Output
# Print the read number and the minimum quantity of each necessary banknotes
# in Portuguese language, as the given example. Do not forget to print the end
# of line after each line, otherwise you will receive “Presentation Error”.
realNumber = int(input())
test = realNumber
note1 = 100
note2 = 50
note3 = 20
note4 = 10
note5 = 5
note6 = 2
note7 = 1

if realNumber >= note1:
    countNote1 = int(realNumber/ note1)
    realNumber = realNumber-(note1*countNote1)
    # print(countNote1)
else:
    countNote1 = 0
    # print(realNumber)
if realNumber >= note2:
    countNote2 = int(realNumber/ note2)
    realNumber = realNumber-(note2*countNote2)
    # print(countNote2)
    # print(realNumber)
else:
    countNote2 = 0

if realNumber >= note3:
    countNote3 = int(realNumber/ note3)
    realNumber = realNumber-(note3*countNote3)
    # print(countNote3)
    # print(realNumber)
else:
    countNote3 = 0

if realNumber >= note4:
    countNote4 = int(realNumber/ note4)
    realNumber = realNumber-(note4*countNote4)
    # print(countNote4)
    # print(realNumber)
else:
    countNote4 = 0

if realNumber >= note5:
    countNote5 = int(realNumber/ note5)
    realNumber = realNumber-(note5*countNote5)
    # print(countnote5)
    # print(realNumber)
else:
    countNote5 = 0

if realNumber >= note6:
    countNote6 = int(realNumber/ note6)
    realNumber = realNumber-(note6*countNote6)
    # print(countnote6)
    # print(realNumber)
else:
    countNote6 = 0

if realNumber >= note7:
    countNote7 = int(realNumber/ note7)
    realNumber = realNumber-(note7*countNote7)
    # print(countnote7)
    # print(realNumber)
else:
    countNote7 = 0

print(test)
print(f'{countNote1} nota(s) de R$ 100,00')
print(f'{countNote2} nota(s) de R$ 50,00')
print(f'{countNote3} nota(s) de R$ 20,00')
print(f'{countNote4} nota(s) de R$ 10,00')
print(f'{countNote5} nota(s) de R$ 5,00')
print(f'{countNote6} nota(s) de R$ 2,00')
print(f'{countNote7} nota(s) de R$ 1,00')


