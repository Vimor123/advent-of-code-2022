class Monkey:
    items = []
    operation = ""
    # Always test divisiblitiy
    test = 0
    # Monkey index
    ifTrue = -1
    ifFalse = -1
    inspectionCount = 0


monkeys = []
monkeyIndex = 0

inputFile = open("input.txt", "r")

for line in inputFile:
    string = line.strip()
    
    if string.startswith("Monkey"):
        monkeys.append(Monkey())
        
    elif string == "":
        monkeyIndex += 1
        
    elif string.startswith("Starting items"):
        startingItems = string[16:]
        startingItems = startingItems.split(", ")
        for i in range(len(startingItems)):
            startingItems[i] = int(startingItems[i])
        monkeys[monkeyIndex].items = startingItems

    elif string.startswith("Operation"):
        monkeys[monkeyIndex].operation = string[17:]

    elif string.startswith("Test"):
        monkeys[monkeyIndex].test = int(string[19:])

    elif string.startswith("If true"):
        monkeys[monkeyIndex].ifTrue = int(string[25:])

    elif string.startswith("If false"):
        monkeys[monkeyIndex].ifFalse = int(string[26:])


for i in range(20):

    for monkey in monkeys:
        items = monkey.items.copy()

        for item in items:
            monkey.inspectionCount += 1
            worryLevel = item
            operationString = monkey.operation
            operationSegments = operationString.split()

            if operationSegments[1] == "+":
                if operationSegments[2] == "old":
                    worryLevel += worryLevel
                else:
                    worryLevel += int(operationSegments[2])

            else:
                if operationSegments[2] == "old":
                    worryLevel *= worryLevel
                else:
                    worryLevel *= int(operationSegments[2])

            worryLevel //= 3

            if worryLevel % monkey.test == 0:
                monkey.items.pop(0)
                monkeys[monkey.ifTrue].items.append(worryLevel)

            else:
                monkey.items.pop(0)
                monkeys[monkey.ifFalse].items.append(worryLevel)


inspectionCounts = []
for monkey in monkeys:
    inspectionCounts.append(monkey.inspectionCount)

maxCount = max(inspectionCounts)
inspectionCounts.remove(maxCount)
maxCount2 = max(inspectionCounts)

print(maxCount * maxCount2)
