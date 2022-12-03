inputFile = open("input.txt", "r")

rucksacks = []

for line in inputFile:
    rucksack = line[:-1]
    firstCompartment = rucksack[:(len(rucksack)//2)]
    secondCompartment = rucksack[(len(rucksack)//2):]
    rucksacks.append([firstCompartment, secondCompartment])

total = 0

for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            if item.islower():
                total += ord(item) - 96
            else:
                total += ord(item) - 64 + 26
            break

print(total)
