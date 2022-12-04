caloriesByElf = [0]
elfIndex = 0

inputFile = open("input.txt", "r")

for line in inputFile:
    number = line[:-1]
    if len(number) == 0:
        caloriesByElf.append(0)
        elfIndex += 1
    else:
        caloriesByElf[elfIndex] += int(line)

inputFile.close()

total = 0
for i in range(3):
    maxCalories = max(caloriesByElf)
    total += maxCalories
    caloriesByElf.remove(maxCalories)

print(total)
