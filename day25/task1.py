inputFile = open("input.txt", "r")

snafuNumbers = []

for line in inputFile:
    snafuNumbers.append(line[:-1])

inputFile.close()

totalFuel = 0

for snafuNumber in snafuNumbers:
    number = 0
    for i in range(len(snafuNumber) - 1, -1, -1):
        character = snafuNumber[i]
        weight = len(snafuNumber) - i - 1
        if character == "2":
            number += 2 * (5 ** weight)
        elif character == "1":
            number += (5 ** weight)
        elif character == "-":
            number -= (5 ** weight)
        elif character == "=":
            number -= 2 * (5 ** weight)
    
    totalFuel += number


number = totalFuel

weight = 1
maxValue = 2

numberString = ""

while maxValue < number:
    weight *= 5
    maxValue += 2 * weight

maxValue -= weight

while weight != 0:
    
    if number > maxValue:
        number -= 2 * weight
        numberString += "2"
    elif number > maxValue - weight:
        number -= weight
        numberString += "1"
    elif number >= -(maxValue-weight):
        numberString += "0"
    elif number >= -maxValue:
        number += weight
        numberString += "-"
    else:
        number += 2 * weight
        numberString += "="
        
    maxValue -= weight
    weight //= 5
    maxValue -= weight

print(numberString)
