inputFile = open("input.txt", "r")

paths = []

for line in inputFile:
    coordsString = line[:-1].split(' -> ')
    coords = []
    for coordString in coordsString:
        coord = coordString.split(',')
        coord[0] = int(coord[0])
        coord[1] = int(coord[1])
        coords.append(coord)
    paths.append(coords)

inputFile.close()


minX = -1
maxX = 0

maxY = 0

for path in paths:
    for coord in path:
        if coord[0] > maxX:
            maxX = coord[0]
        elif coord[0] < minX or minX == -1:
            minX = coord[0]

        if coord[1] > maxY:
            maxY = coord[1]


cave = []

for i in range(maxY + 1 + 1):
    cave.append(['.'] * 750)

cave.append(['#'] * 750)


for path in paths:

    for i in range(len(path) - 1):
        currPosition = path[i]
        nextPosition = path[i+1]

        if currPosition[0] == nextPosition[0]:
            toCoord = max(currPosition[1], nextPosition[1])
            fromCoord = min(currPosition[1], nextPosition[1])
            
            for j in range(fromCoord, toCoord + 1):
                cave[j][currPosition[0]] = "#"

        elif currPosition[1] == nextPosition[1]:
            toCoord = max(currPosition[0], nextPosition[0])
            fromCoord = min(currPosition[0], nextPosition[0])

            for j in range(fromCoord, toCoord + 1):
                cave[currPosition[1]][j] = "#"



def throwSand():
    throwSandStartingX = 500

    sandCoords = [throwSandStartingX, 0]

    stopped = False

    noMore = False

    while not stopped:
        if sandCoords[1] >= len(cave):
            stopped = True
            noMore = True
            
        elif cave[sandCoords[1] + 1][sandCoords[0]] == ".":
            sandCoords[1] += 1
            
        elif sandCoords[0] <= 0:
            stopped = True
            noMore = True

        elif cave[sandCoords[1] + 1][sandCoords[0] - 1] == ".":
            sandCoords[0] -= 1
            sandCoords[1] += 1

        elif sandCoords[0] >= len(cave[0]):
            stopped = True
            noMore = True

        elif cave[sandCoords[1] + 1][sandCoords[0] + 1] == ".":
            sandCoords[0] += 1
            sandCoords[1] += 1

        else:
            cave[sandCoords[1]][sandCoords[0]] = "O"
            stopped = True

        if cave[0][500] == "O":
            stopped = True
            noMore = True

    return noMore


noOfUnits = 0

filled = False

while not filled:
    filled = throwSand()
    noOfUnits += 1

print(noOfUnits)


'''      
for i in range(len(cave)):
    print('')
    for j in range(len(cave[0])):
        print(cave[i][j], end = '')
'''
