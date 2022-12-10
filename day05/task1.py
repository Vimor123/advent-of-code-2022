inputFile = open("input.txt", "r")

stackRows = []
instructionRows = []

parsePhase = "stacks"

for line in inputFile:
    if parsePhase == "stacks":
        if line[:-1] == "":
            parsePhase = "instructions"
        else:
            stackRows.append(line[:-1])
    elif parsePhase == "instructions":
        instructionRows.append(line[:-1])

inputFile.close()

# Forming stacks

stacks = []
noOfStacks = (len(stackRows[0]) + 1)//4

for i in range(noOfStacks):
    stacks.append([])

for rowIndex in range(len(stackRows)-2, -1, -1):
    for stackIndex in range(noOfStacks):
        stackRow = stackRows[rowIndex]
        stackElement = stackRow[(stackIndex * 4):(stackIndex * 4 + 3)]
        if stackElement != "   ":
            stacks[stackIndex].append(stackElement[1])

# Following instructions

for instruction in instructionRows:
    instructionSegments = instruction.split()
    noOfMoves = int(instructionSegments[1])
    fromStack = int(instructionSegments[3]) - 1
    toStack = int(instructionSegments[5]) - 1

    for i in range(noOfMoves):
        removedElement = stacks[fromStack].pop(len(stacks[fromStack]) - 1)
        stacks[toStack].append(removedElement)

# Printing result

for stack in stacks:
    print(stack[len(stack) - 1], end="")
