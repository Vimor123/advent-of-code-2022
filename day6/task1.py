inputFile = open("input.txt", "r")

inputString = inputFile.read()

inputFile.close()

for i in range(3, len(inputString) - 1):
    packetSet = { inputString[i-3], inputString[i-2], inputString[i-1], inputString[i]}
    if len(packetSet) == 4:
        print(i+1)
        break
