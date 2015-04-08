# coding=utf-8
__author__ = 'Eli Sobylak'
__created__ = '7-Apr-2015'

# Take an input from the user and parse into four values and store as variables.
# make a definition to use those variables as inputs and output the value and add thier result to a temporary number
# to store the total resistor value

colorBands = raw_input("Please enter the colors of a 4-band resistor--(Colors begin with capital letters):")
colorList = []
colorList = colorBands.split(' ')

firstBand = colorList[0]
secondBand = colorList[1]
thirdBand = colorList[2]
fourthBand = colorList[3]


def mathFirst(x):
    total = 0
    if x == 'Black':
        total += 0
    elif x == 'Brown':
        total += 100
    elif x == 'Red':
        total += 200
    elif x == 'Orange':
        total += 300
    elif x == 'Yellow':
        total += 400
    elif x == 'Green':
        total += 500
    elif x == 'Blue':
        total += 600
    elif x == 'Violet':
        total += 700
    elif x == 'Grey':
        total += 800
    elif x == 'White':
        total += 900
    elif x == 'Gold':
        print('This color cannot be a 1st-band color')
    elif x == 'Siler':
        print('This color cannot be a 1st-band color')
    #print (total)
    return total


def mathSecond(x):
    total = 0
    if x == 'Black':
        total += 0
    elif x == 'Brown':
        total += 10
    elif x == 'Red':
        total += 20
    elif x == 'Orange':
        total += 30
    elif x == 'Yellow':
        total += 40
    elif x == 'Green':
        total += 50
    elif x == 'Blue':
        total += 60
    elif x == 'Violet':
        total += 70
    elif x == 'Grey':
        total += 80
    elif x == 'White':
        total += 90
    elif x == 'Gold':
        print('This color cannot be a 2nd-band color')
    elif x == 'Siler':
        print('This color cannot be a 2nd-band color')
    #print (total)
    return total

def multiply(x):
    total = 0
    if x == 'Black':
        total += 1
    elif x == 'Brown':
        total += 10
    elif x == 'Red':
        total += 100
    elif x == 'Orange':
        total += 1000
    elif x == 'Yellow':
        total += 10000
    elif x == 'Green':
        total += 100000
    elif x == 'Blue':
        total += 1000000
    elif x == 'Violet':
        total += 10000000
    elif x == 'Grey':
        print('This color cannot be a multiplier')
    elif x == 'White':
        print('This color cannot be a multiplier')
    elif x == 'Gold':
        total += 0.1
    elif x == 'Siler':
        total += 0.01
    #print (total)
    return total


def tolerance(x):
    total = 0
    if x == 'Black':
        print('This color cannot be a 4th-band color')
    elif x == 'Brown':
        total += 1
    elif x == 'Red':
        total += 2
    elif x == 'Orange':
        print('This color cannot be a 4th-band color')
    elif x == 'Yellow':
        print('This color cannot be a 4th-band color')
    elif x == 'Green':
        total += 0.5
    elif x == 'Blue':
        total += 0.25
    elif x == 'Violet':
        total += 0.10
    elif x == 'Grey':
        total += 0.05
    elif x == 'White':
        print('This color cannot be a 4th-band color')
    elif x == 'Gold':
        total += 5
    elif x == 'Siler':
        total += 10
    #print (total)
    return total


def main():
    mathFirst(firstBand)
    mathSecond(secondBand)
    multiply(thirdBand)
    tolerance(fourthBand)

main()

total = ((mathFirst(firstBand)) + (mathSecond(secondBand))) * (multiply(thirdBand))
toleranceLevel = tolerance(fourthBand)

print 'You have a ' + str(total) + ' Ohm resistor!'
print 'With a tolerance of about ' + '± ' + str(toleranceLevel) + '%'