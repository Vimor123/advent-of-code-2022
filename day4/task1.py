inputFile = open("input.txt", "r")

elfPairs = []

for line in inputFile:
    pairString = line[:-1]
    pair = pairString.split(',')
    firstElf = pair[0].split('-')
    secondElf = pair[1].split('-')

    for i in range(2):
        firstElf[i] = int(firstElf[i])
        secondElf[i] = int(secondElf[i])

    elfPairs.append([firstElf, secondElf])

inputFile.close()

noOfFullyContained = 0

for elfPair in elfPairs:
    if elfPair[0][0] > elfPair[1][0]:
        if elfPair [0][1] <= elfPair[1][1]:
            noOfFullyContained += 1
    elif elfPair [0][0] < elfPair [1][0]:
        if elfPair [0][1] >= elfPair[1][1]:
            noOfFullyContained += 1
    else:
        noOfFullyContained += 1

print(noOfFullyContained)
