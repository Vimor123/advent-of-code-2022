inputFile = open("input.txt", "r")

droplets = []

maxX = 0
maxY = 0
maxZ = 0

for line in inputFile:
    droplet = line[:-1].split(',')
    for i in range(len(droplet)):
        droplet[i] = int(droplet[i])
    if droplet[0] > maxX:
        maxX = droplet[0]
    if droplet[1] > maxY:
        maxY = droplet[1]
    if droplet[2] > maxZ:
        maxZ = droplet[2]
    droplets.append(droplet)

inputFile.close()


dropletMatrix = []

for i in range(maxX + 1):
    dropletMatrix.append([])
    for j in range(maxY + 1):
        dropletMatrix[i].append([])
        for k in range(maxZ + 1):
            dropletMatrix[i][j].append(".")

for droplet in droplets:
    dropletMatrix[droplet[0]][droplet[1]][droplet[2]] = "#"


noOfSurfaces = 0

for i in range(maxX + 1):
    for j in range(maxY + 1):
        for k in range(maxZ + 1):
            if dropletMatrix[i][j][k] == "#":
                noOfTouchingSides = 0
                if i > 0:
                    if dropletMatrix[i - 1][j][k] == "#":
                        noOfTouchingSides += 1
                if i < maxX:
                    if dropletMatrix[i + 1][j][k] == "#":
                        noOfTouchingSides += 1
                if j > 0:
                    if dropletMatrix[i][j - 1][k] == "#":
                        noOfTouchingSides += 1
                if j < maxY:
                    if dropletMatrix[i][j + 1][k] == "#":
                        noOfTouchingSides += 1
                if k > 0:
                    if dropletMatrix[i][j][k - 1] == "#":
                        noOfTouchingSides += 1
                if k < maxZ:
                    if dropletMatrix[i][j][k + 1] == "#":
                        noOfTouchingSides += 1
                
                noOfSurfaces += 6 - noOfTouchingSides
                

print(noOfSurfaces)

"""
for i in range(maxX + 1):
    print('')
    for j in range(maxY + 1):
        print('')
        for k in range(maxZ + 1):
            print(dropletMatrix[i][j][k], end = '')
"""
