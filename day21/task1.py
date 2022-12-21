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
    
    monkeys[monkeyName] = monkey

inputFile.close()


while monkeys["root"]["value"] == "N":
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

print(monkeys["root"]["value"])
