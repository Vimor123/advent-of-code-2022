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


targetRows = []
for i in range(0, 4000000+1):
    targetRows.append(i)

positionX = 0
positionY = 0

for targetRow in targetRows:

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

    rowFound = True
    for finalRange in finalRanges:
        if finalRange[0] <= 0 and finalRange[1] >= 4000000:
            rowFound = False

    if rowFound:
        print("Found a position")
        for finalRange in finalRanges:
            if finalRange[1] <= 4000000:
                positionX = finalRange[1] + 1
        print("X =", positionX)
        positionY = targetRow
        print("Y =", positionY)
        break

    if targetRow % 100000 == 0:
        print("Still searching, just finished with row", targetRow)

print("Tuning frequency:", positionX * 4000000 + positionY)
