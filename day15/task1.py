inputFile = open("input.txt", "r")

sensorBeacons = []

for line in inputFile:
    sensorLine, beaconLine = map(str, line[:-1].split(':'))

    sensorString = sensorLine[sensorLine.index("x"):]
    beaconString = beaconLine[beaconLine.index("x"):]

    sensorStringCoords = sensorString.split(', ')
    beaconStringCoords = beaconString.split(', ')

    sensorCoordX = int(sensorStringCoords[0][2:])
    sensorCoordY = int(sensorStringCoords[1][2:])

    beaconCoordX = int(beaconStringCoords[0][2:])
    beaconCoordY = int(beaconStringCoords[1][2:])

    sensorBeacons.append({ "sensor" : [sensorCoordX, sensorCoordY],
                           "beacon" : [beaconCoordX, beaconCoordY]})

inputFile.close()


def calculateDistance(sensor, beacon):
    xDistance = abs(sensor[0] - beacon[0])
    yDistance = abs(sensor[1] - beacon[1])
    return xDistance + yDistance


targetRow = 2000000

rowRanges = []

for sensorBeacon in sensorBeacons:
    sensor = sensorBeacon["sensor"]
    beacon = sensorBeacon["beacon"]
    
    maxDistance = calculateDistance(sensor, beacon)

    distanceFromTargetRow = abs(sensor[1] - targetRow)

    if abs(distanceFromTargetRow) <= maxDistance:

        centerOfRange = sensor[0]
        noOfLeftAndRight = maxDistance - distanceFromTargetRow


        leftRange = centerOfRange - noOfLeftAndRight
        rightRange = centerOfRange + noOfLeftAndRight
        
        rowRanges.append([leftRange, rightRange])


rowRanges.sort()

"""
for rowRange in rowRanges:
    print(rowRange)

print("")
"""

finalRanges = [rowRanges[0]]

for i in range(1, len(rowRanges)):

    rowRange = rowRanges[i]

    for j in range(len(finalRanges)):

        if rowRange[0] <= finalRanges[j][1]:
            if rowRange[1] <= finalRanges[j][1]:
                pass
            else:
                finalRanges[j][1] = rowRange[1]

                for k in range(j + 1, len(finalRanges)):

                    if finalRanges[j][1] >= finalRanges[j+1][0]:

                        if finalRanges[j][1] <= finalRanges[j+1][1]:
                            finalRanges[j][1] = finalRanges[j+1][1]
                            finalRanges.pop(j+1)
                            break

                        else:
                            finalRanges.pop(j+1)

                    else:
                        break

            break

        else:
            if j >= len(finalRanges) - 1:
                finalRanges.append(rowRange)
                break

    #print(finalRanges)

"""
print("")

for finalRange in finalRanges:
    print(finalRange)
"""

noOfPositions = 0

noOfObjectsInTargetRow = 0

objects = []

for sensorBeacon in sensorBeacons:

    sensor = sensorBeacon["sensor"]
    beacon = sensorBeacon["beacon"]

    if sensor[1] == targetRow:
        if sensor not in objects:
            objects.append(sensor)

    if beacon[1] == targetRow:
        if beacon not in objects:
            objects.append(beacon)

for obj in objects:
    for finalRange in finalRanges:
        if obj[0] >= finalRange[0] and obj[0] <= finalRange[1]:
            noOfObjectsInTargetRow += 1
            break

for finalRange in finalRanges:
    noOfPositions += finalRange[1] - finalRange[0] + 1


noOfPositions -= noOfObjectsInTargetRow

print(noOfPositions)
