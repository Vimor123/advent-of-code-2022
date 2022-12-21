inputFile = open("input.txt", "r")

monkeys = {}

for line in inputFile:
    monkeySegments = line[:-1].split(": ")

    monkeyName = monkeySegments[0]
    
    monkeyValue = "N"
    monkeyOperation = "Number"
    if monkeySegments[1].isnumeric():
        monkeyValue = int(monkeySegments[1])
    else:
        monkeyOperation = monkeySegments[1]

    monkey = { "value" : monkeyValue,
               "operation" : monkeyOperation }

    if monkeyName != "root" and monkeyName != "humn":
        monkeys[monkeyName] = monkey
    elif monkeyName == "root":
        rootMonkey = monkey
    elif monkeyName == "humn":
        humanMonkey = monkey

inputFile.close()

numberFound = False
magicNumber = 3375719472700
# Running the program until i get it to display similar values

monkeysCopy = {}
for monkey in monkeys:
    monkeysCopy[monkey] = monkeys[monkey].copy()

while not numberFound:

    monkeys = {}
    for monkey in monkeysCopy:
        monkeys[monkey] = monkeysCopy[monkey].copy()

    operationRoot = rootMonkey["operation"].split()
    monkey1Name = operationRoot[0]
    monkey2Name = operationRoot[2]

    humanMonkey["value"] = magicNumber

    monkeys["humn"] = humanMonkey

    while monkeys[monkey1Name]["value"] == "N" or monkeys[monkey2Name]["value"] == "N":
        for monkey in monkeys:
            if monkeys[monkey]["operation"] != "Number":
                monkeyOperationString = monkeys[monkey]["operation"]
                monkeyOperationSegments = monkeyOperationString.split()
                monkey1 = monkeys[monkeyOperationSegments[0]]
                operation = monkeyOperationSegments[1]
                monkey2 = monkeys[monkeyOperationSegments[2]]
                if monkey1["value"] != "N" and monkey2["value"] != "N":
                    if operation == "+":
                        monkeys[monkey]["value"] = monkey1["value"] + monkey2["value"]
                    elif operation == "-":
                        monkeys[monkey]["value"] = monkey1["value"] - monkey2["value"]
                    elif operation == "*":
                        monkeys[monkey]["value"] = monkey1["value"] * monkey2["value"]
                    elif operation == "/":
                        monkeys[monkey]["value"] = monkey1["value"] // monkey2["value"]
                    monkeys[monkey]["operation"] = "Number"

    if monkeys[monkey1Name]["value"] == monkeys[monkey2Name]["value"]:
        numberFound = True
        break

    #print(magicNumber, monkeys[monkey1Name]["value"], monkeys[monkey2Name]["value"])

    magicNumber += 1

print(magicNumber)
