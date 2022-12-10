inputFile = open("input.txt", "r")

instructions = []

for line in inputFile:
    instructions.append(line[:-1])

inputFile.close()
        

x = 1

cycle = 0

screen = []


def drawPixel(cycle, x):
    global screen
    if (cycle - 1) % 40 in range(x-1, x+2):
        screen.append("#")
    else:
        screen.append(".")


for instruction in instructions:

    if instruction == "noop":
        cycle += 1
        drawPixel(cycle, x)

    elif instruction.startswith("addx"):
        cycle += 1
        drawPixel(cycle, x)

        cycle += 1
        drawPixel(cycle, x)
        instructionComponents = instruction.split()
        x += int(instructionComponents[1])


for i in range(6):
    print("")
    for j in range(40):
        print(screen[i * 40 + j], end = "")
