import sys

sys.setrecursionlimit(1000000)

inputFile = open("input.txt", "r")

heightMap = []

for line in inputFile:
    heightMap.append(list(line[:-1]))

inputFile.close()


for i in range(len(heightMap)):
    for j in range(len(heightMap[0])):
        heightMap[i][j] = [heightMap[i][j], 100000]
        if heightMap[i][j][0] == "S":
            startingPosition = [i, j]
            heightMap[i][j][0] = "a"
        elif heightMap[i][j][0] == "E":
            endingPosition = [i, j]
            heightMap[i][j][0] = "z"

"""
for i in range(len(heightMap)):
    print("")
    for j in range(len(heightMap[0])):
        if heightMap[i][j][0] == "a" or heightMap[i][j][0] == "b":
            print(heightMap[i][j][0], end = "")
        else:
            print("-", end = "")
"""


def paintDot(prevPosition, position):

    global heightMap

    height = heightMap[position[0]][position[1]][0]

    steps = heightMap[position[0]][position[1]][1]

    prevHeight = heightMap[prevPosition[0]][prevPosition[1]][0]

    prevSteps = heightMap[prevPosition[0]][prevPosition[1]][1]
    
    if ord(height) <= ord(prevHeight) + 1 and steps > prevSteps + 1:
        heightMap[position[0]][position[1]][1] = prevSteps + 1

    else:
        return

    newPosition1 = [position[0]-1, position[1]]
    if newPosition1[0] >= 0:
        paintDot(position, newPosition1)

    newPosition2 = [position[0]+1, position[1]]
    if newPosition2[0] < len(heightMap):
        paintDot(position, newPosition2)

    newPosition3 = [position[0], position[1]-1]
    if newPosition3[1] >= 0:
        paintDot(position, newPosition3)

    newPosition4 = [position[0], position[1]+1]
    if newPosition4[1] < len(heightMap[0]):
        paintDot(position, newPosition4)

startingPosition = [14, 0]
heightMap[startingPosition[0]][startingPosition[1]][1] = 0
paintDot(startingPosition, [startingPosition[0], startingPosition[1]+1])

print("")

print(heightMap[endingPosition[0]][endingPosition[1]][1])


