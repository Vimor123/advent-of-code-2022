inputFile = open("input.txt", "r")

blizzardMap = []

for line in inputFile:
    blizzardMap.append(list(line[:-1]))

inputFile.close()

blizzards = []

for i in range(len(blizzardMap)):
    for j in range(len(blizzardMap[0])):
        blizzardDirection = "None"
        if blizzardMap[i][j] == ">":
            blizzardDirection = "E"
        elif blizzardMap[i][j] == "<":
            blizzardDirection = "W"
        elif blizzardMap[i][j] == "v":
            blizzardDirection = "S"
        elif blizzardMap[i][j] == "^":
            blizzardDirection = "N"

        if blizzardDirection != "None":
            blizzards.append ({ "direction" : blizzardDirection,
                                "position" : [i, j] })


for i in range(len(blizzardMap)):
    for j in range(len(blizzardMap[0])):
        if blizzardMap[i][j] != "." and blizzardMap[i][j] != "#":
            blizzardMap[i][j] = "O"

positions = [[0, 1]]

endingPosition = [len(blizzardMap) - 1, len(blizzardMap[0]) - 2]

time = 0

while endingPosition not in positions:
    
    time += 1

    for i in range(len(blizzardMap)):
        for j in range(len(blizzardMap[0])):
            if blizzardMap[i][j] == "O":
                blizzardMap[i][j] = "."

    for blizzard in blizzards:
        blizzardDirection = blizzard["direction"]
        blizzardPosition = blizzard["position"]

        if blizzardDirection == "N":
            if blizzardPosition[0] == 1:
                blizzard["position"] = [len(blizzardMap) - 2, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] - 1, blizzardPosition[1]]

        elif blizzardDirection == "S":
            if blizzardPosition[0] == len(blizzardMap) - 2:
                blizzard["position"] = [1, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] + 1, blizzardPosition[1]]

        elif blizzardDirection == "E":
            if blizzardPosition[1] == len(blizzardMap[0]) - 2:
                blizzard["position"] = [blizzardPosition[0], 1]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] + 1]

        elif blizzardDirection == "W":
            if blizzardPosition[1] == 1:
                blizzard["position"] = [blizzardPosition[0], len(blizzardMap[0]) - 2]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] - 1]

    for blizzard in blizzards:
        blizzardPosition = blizzard["position"]
        blizzardMap[blizzardPosition[0]][blizzardPosition[1]] = "O"

    """
    for i in range(len(blizzardMap)):
        print("")
        for j in range(len(blizzardMap[0])):
            print(blizzardMap[i][j], end = "")
    """

    newPositions = []

    for position in positions:
        if blizzardMap[position[0]][position[1]] == "." and [position[0], position[1]] not in newPositions:
            newPositions.append([position[0], position[1]])
        if blizzardMap[position[0] + 1][position[1]] == "." and [position[0] + 1, position[1]] not in newPositions:
            newPositions.append([position[0] + 1, position[1]])
        if position[0] > 0:
            if blizzardMap[position[0] - 1][position[1]] == "." and [position[0] - 1, position[1]] not in newPositions:
                newPositions.append([position[0] - 1, position[1]])
        if blizzardMap[position[0]][position[1] + 1] == "." and [position[0], position[1] + 1] not in newPositions:
            newPositions.append([position[0], position[1] + 1])
        if blizzardMap[position[0]][position[1] - 1] == "." and [position[0], position[1] - 1] not in newPositions:
            newPositions.append([position[0], position[1] - 1])

    positions = newPositions

print("First point:", time)


endingPosition = [0, 1]

positions = [[len(blizzardMap) - 1, len(blizzardMap[0]) - 2]]

while endingPosition not in positions:
    
    time += 1

    for i in range(len(blizzardMap)):
        for j in range(len(blizzardMap[0])):
            if blizzardMap[i][j] == "O":
                blizzardMap[i][j] = "."

    for blizzard in blizzards:
        blizzardDirection = blizzard["direction"]
        blizzardPosition = blizzard["position"]

        if blizzardDirection == "N":
            if blizzardPosition[0] == 1:
                blizzard["position"] = [len(blizzardMap) - 2, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] - 1, blizzardPosition[1]]

        elif blizzardDirection == "S":
            if blizzardPosition[0] == len(blizzardMap) - 2:
                blizzard["position"] = [1, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] + 1, blizzardPosition[1]]

        elif blizzardDirection == "E":
            if blizzardPosition[1] == len(blizzardMap[0]) - 2:
                blizzard["position"] = [blizzardPosition[0], 1]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] + 1]

        elif blizzardDirection == "W":
            if blizzardPosition[1] == 1:
                blizzard["position"] = [blizzardPosition[0], len(blizzardMap[0]) - 2]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] - 1]

    for blizzard in blizzards:
        blizzardPosition = blizzard["position"]
        blizzardMap[blizzardPosition[0]][blizzardPosition[1]] = "O"

    """
    for i in range(len(blizzardMap)):
        print("")
        for j in range(len(blizzardMap[0])):
            print(blizzardMap[i][j], end = "")
    """

    newPositions = []

    for position in positions:
        if blizzardMap[position[0]][position[1]] == "." and [position[0], position[1]] not in newPositions:
            newPositions.append([position[0], position[1]])
        if position[0] < len(blizzardMap) - 1:
            if blizzardMap[position[0] + 1][position[1]] == "." and [position[0] + 1, position[1]] not in newPositions:
                newPositions.append([position[0] + 1, position[1]])
        if blizzardMap[position[0] - 1][position[1]] == "." and [position[0] - 1, position[1]] not in newPositions:
            newPositions.append([position[0] - 1, position[1]])
        if blizzardMap[position[0]][position[1] + 1] == "." and [position[0], position[1] + 1] not in newPositions:
            newPositions.append([position[0], position[1] + 1])
        if blizzardMap[position[0]][position[1] - 1] == "." and [position[0], position[1] - 1] not in newPositions:
            newPositions.append([position[0], position[1] - 1])

    positions = newPositions

print("Second point:", time)


positions = [[0, 1]]

endingPosition = [len(blizzardMap) - 1, len(blizzardMap[0]) - 2]

while endingPosition not in positions:
    
    time += 1

    for i in range(len(blizzardMap)):
        for j in range(len(blizzardMap[0])):
            if blizzardMap[i][j] == "O":
                blizzardMap[i][j] = "."

    for blizzard in blizzards:
        blizzardDirection = blizzard["direction"]
        blizzardPosition = blizzard["position"]

        if blizzardDirection == "N":
            if blizzardPosition[0] == 1:
                blizzard["position"] = [len(blizzardMap) - 2, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] - 1, blizzardPosition[1]]

        elif blizzardDirection == "S":
            if blizzardPosition[0] == len(blizzardMap) - 2:
                blizzard["position"] = [1, blizzardPosition[1]]
            else:
                blizzard["position"] = [blizzardPosition[0] + 1, blizzardPosition[1]]

        elif blizzardDirection == "E":
            if blizzardPosition[1] == len(blizzardMap[0]) - 2:
                blizzard["position"] = [blizzardPosition[0], 1]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] + 1]

        elif blizzardDirection == "W":
            if blizzardPosition[1] == 1:
                blizzard["position"] = [blizzardPosition[0], len(blizzardMap[0]) - 2]
            else:
                blizzard["position"] = [blizzardPosition[0], blizzardPosition[1] - 1]

    for blizzard in blizzards:
        blizzardPosition = blizzard["position"]
        blizzardMap[blizzardPosition[0]][blizzardPosition[1]] = "O"

    """
    for i in range(len(blizzardMap)):
        print("")
        for j in range(len(blizzardMap[0])):
            print(blizzardMap[i][j], end = "")
    """

    newPositions = []

    for position in positions:
        if blizzardMap[position[0]][position[1]] == "." and [position[0], position[1]] not in newPositions:
            newPositions.append([position[0], position[1]])
        if blizzardMap[position[0] + 1][position[1]] == "." and [position[0] + 1, position[1]] not in newPositions:
            newPositions.append([position[0] + 1, position[1]])
        if position[0] > 0:
            if blizzardMap[position[0] - 1][position[1]] == "." and [position[0] - 1, position[1]] not in newPositions:
                newPositions.append([position[0] - 1, position[1]])
        if blizzardMap[position[0]][position[1] + 1] == "." and [position[0], position[1] + 1] not in newPositions:
            newPositions.append([position[0], position[1] + 1])
        if blizzardMap[position[0]][position[1] - 1] == "." and [position[0], position[1] - 1] not in newPositions:
            newPositions.append([position[0], position[1] - 1])

    positions = newPositions

print("End:", time)
