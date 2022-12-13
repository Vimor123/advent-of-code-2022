inputFile = open("input.txt", "r")

packets = []

for line in inputFile:
    if line != "\n":
        packets.append(line[:-1])

inputFile.close()

packets.append("[[2]]")
packets.append("[[6]]")

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



packetsSorted = False

while not packetsSorted:

    packetsSorted = True

    for i in range(len(packets) - 1):
        packet1 = packets[i]
        packet2 = packets[i+1]

        copiedPacket1 = eval(packet1)
        copiedPacket2 = eval(packet2)

        orderCorrect = pairCheck(copiedPacket1, copiedPacket2)
        if orderCorrect == 0:
            packets[i+1] = packet1
            packets[i] = packet2
            packetsSorted = False

packetDivider1Index = packets.index("[[2]]") + 1
packetDivider2Index = packets.index("[[6]]") + 1

print(packetDivider1Index * packetDivider2Index)
