inputFile = open("input.txt", "r")

packetPairs = [[]]

packetPairIndex = 0

for line in inputFile:
    if line == "\n":
        packetPairs.append([])
        packetPairIndex += 1
    else:
        packetPairs[packetPairIndex].append(line[:-1])

inputFile.close()



def pairCheck(packet1, packet2):

    parsed = False

    # 0 - incorrect, 1 - undefined, 2 - correct
    correctOrder = 1

    while not parsed:
        if len(packet1) == 0 and len(packet2) == 0:
            return 1
        elif len(packet1) == 0:
            return 2
        elif len(packet2) == 0:
            return 0
        
        element1 = packet1.pop(0)
        element2 = packet2.pop(0)

        if type(element1) is int:
            
            if type(element2) is int:
                if element1 > element2:
                    return 0
                elif element1 < element2:
                    return 2
                
            elif type(element2) is list:
                correctOrderOfLists = pairCheck([element1], element2)
                if correctOrderOfLists == 0:
                    return 0
                elif correctOrderOfLists == 2:
                    return 2

        elif type(element1) is list:

            if type(element2) is int:
                correctOrderOfLists = pairCheck(element1, [element2])
                if correctOrderOfLists == 0:
                    return 0
                elif correctOrderOfLists == 2:
                    return 2

            elif type(element2) is list:

                correctOrderOfLists = pairCheck(element1, element2)
                if correctOrderOfLists == 0:
                    return 0
                elif correctOrderOfLists == 2:
                    return 2



sumOfPacketIndexes = 0

for packetIndex in range(len(packetPairs)):

    packetPair = packetPairs[packetIndex]

    packet1 = eval(packetPair[0])
    packet2 = eval(packetPair[1])

    correctOrder = pairCheck(packet1, packet2)

    if correctOrder == 2:
        sumOfPacketIndexes += packetIndex + 1

print(sumOfPacketIndexes)
