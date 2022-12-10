inputFile = open("input.txt", "r")

instructions = []

for line in inputFile:
    instructions.append(line[:-1])

inputFile.close()
        

x = 1

cycle = 0

signalStrengths = []


for instruction in instructions:

    if instruction == "noop":
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signalStrengths.append(cycle * x)

    elif instruction.startswith("addx"):
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signalStrengths.append(cycle * x)

        cycle += 1
        if (cycle - 20) % 40 == 0:
            signalStrengths.append(cycle * x)
        instructionComponents = instruction.split()
        x += int(instructionComponents[1])

print(sum(signalStrengths))
