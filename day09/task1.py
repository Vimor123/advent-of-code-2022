inputFile = open("input.txt", "r")

instructions = []

for line in inputFile:
    instructions.append(line[:-1])

inputFile.close()


coordinatesVisitedByTail = []

coordsHead = [0, 0]
coordsTail = [0, 0]

for instruction in instructions:
    direction, noOfMoves = map(str, instruction.split())
    noOfMoves = int(noOfMoves)

    for i in range(noOfMoves):
        
        if direction == "L":
            coordsHead[1] -= 1

        elif direction == "R":
            coordsHead[1] += 1

        elif direction == "U":
            coordsHead[0] += 1

        elif direction == "D":
            coordsHead[0] -= 1


        if abs(coordsHead[0] - coordsTail[0]) > 1 and abs(coordsHead[1] - coordsTail[1]) > 0:
            if coordsHead[0] - coordsTail[0] > 0:
                coordsTail[0] = coordsHead[0] - 1
                coordsTail[1] = coordsHead[1]
            else:
                coordsTail[0] = coordsHead[0] + 1
                coordsTail[1] = coordsHead[1]

        elif abs(coordsHead[1] - coordsTail[1]) > 1 and abs(coordsHead[0] - coordsTail[0]) > 0:
            if coordsHead[1] - coordsTail[1] > 0:
                coordsTail[1] = coordsHead[1] - 1
                coordsTail[0] = coordsHead[0]
            else:
                coordsTail[1] = coordsHead[1] + 1
                coordsTail[0] = coordsHead[0]

        elif abs(coordsHead[0] - coordsTail[0]) > 1 and abs(coordsHead[1] - coordsTail[1]) == 0:
            if coordsHead[0] - coordsTail[0] > 0:
                coordsTail[0] = coordsHead[0] - 1
            else:
                coordsTail[0] = coordsHead[0] + 1

        elif abs(coordsHead[1] - coordsTail[1]) > 1 and abs(coordsHead[0] - coordsTail[0]) == 0:
            if coordsHead[1] - coordsTail[1] > 0:
                coordsTail[1] = coordsHead[1] - 1
            else:
                coordsTail[1] = coordsHead[1] + 1

        coordinateString = "{}, {}".format(coordsTail[0], coordsTail[1])

        if coordinateString not in coordinatesVisitedByTail:
            coordinatesVisitedByTail.append(coordinateString)

print(len(coordinatesVisitedByTail))
