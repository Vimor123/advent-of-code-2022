inputFile = open("input.txt", "r")

instructions = []

for line in inputFile:
    instructions.append(line[:-1])

inputFile.close()


coordinatesVisitedByTail = []

coordsString = []

for i in range(10):
    coordsString.append([0, 0])

for instruction in instructions:
    direction, noOfMoves = map(str, instruction.split())
    noOfMoves = int(noOfMoves)

    for i in range(noOfMoves):
        
        if direction == "L":
            coordsString[0][1] -= 1

        elif direction == "R":
            coordsString[0][1] += 1

        elif direction == "U":
            coordsString[0][0] += 1

        elif direction == "D":
            coordsString[0][0] -= 1


        for i in range(9):

            if abs(coordsString[i][0] - coordsString[i+1][0]) > 1 and abs(coordsString[i][1] - coordsString[i+1][1]) > 1:
                if coordsString[i][0] - coordsString[i+1][0] > 0:
                    coordsString[i+1][0] = coordsString[i][0] - 1
                else:
                    coordsString[i+1][0] = coordsString[i][0] + 1
                if coordsString[i][1] - coordsString[i+1][1] > 0:
                    coordsString[i+1][1] = coordsString[i][1] - 1
                else:
                    coordsString[i+1][1] = coordsString[i][1] + 1

            elif abs(coordsString[i][0] - coordsString[i+1][0]) > 1 and abs(coordsString[i][1] - coordsString[i+1][1]) > 0:
                if coordsString[i][0] - coordsString[i+1][0] > 0:
                    coordsString[i+1][0] = coordsString[i][0] - 1
                    coordsString[i+1][1] = coordsString[i][1]
                else:
                    coordsString[i+1][0] = coordsString[i][0] + 1
                    coordsString[i+1][1] = coordsString[i][1]

            elif abs(coordsString[i][1] - coordsString[i+1][1]) > 1 and abs(coordsString[i][0] - coordsString[i+1][0]) > 0:
                if coordsString[i][1] - coordsString[i+1][1] > 0:
                    coordsString[i+1][1] = coordsString[i][1] - 1
                    coordsString[i+1][0] = coordsString[i][0]
                else:
                    coordsString[i+1][1] = coordsString[i][1] + 1
                    coordsString[i+1][0] = coordsString[i][0]

            elif abs(coordsString[i][0] - coordsString[i+1][0]) > 1 and abs(coordsString[i][1] - coordsString[i+1][1]) == 0:
                if coordsString[i][0] - coordsString[i+1][0] > 0:
                    coordsString[i+1][0] = coordsString[i][0] - 1
                else:
                    coordsString[i+1][0] = coordsString[i][0] + 1

            elif abs(coordsString[i][1] - coordsString[i+1][1]) > 1 and abs(coordsString[i][0] - coordsString[i+1][0]) == 0:
                if coordsString[i][1] - coordsString[i+1][1] > 0:
                    coordsString[i+1][1] = coordsString[i][1] - 1
                else:
                    coordsString[i+1][1] = coordsString[i][1] + 1

        coordinateString = "{}, {}".format(coordsString[9][0], coordsString[9][1])

        if coordinateString not in coordinatesVisitedByTail:
            coordinatesVisitedByTail.append(coordinateString)

print(len(coordinatesVisitedByTail))
