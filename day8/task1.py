inputFile = open("input.txt", "r")

trees = []

for line in inputFile:
    numbers = line[:-1]
    treeHeights = []
    for digit in numbers:
        treeHeights.append(int(digit))
    trees.append(treeHeights)

inputFile.close()


noOfRows = len(trees)
noOfColumns = len(trees[0])

noOfVisibleTrees = 2 * noOfRows + 2 * (noOfColumns - 2)

for rowIndex in range(1, len(trees) - 1):

    for columnIndex in range(1, len(trees[0]) - 1):

        treeHeight = trees[rowIndex][columnIndex]

        isVisible = False
        
        # Top
        isVisibleFromTop = True
        for i in range(0, rowIndex):
            if trees[i][columnIndex] >= treeHeight:
                isVisibleFromTop = False
                break

        if isVisibleFromTop:
            isVisible = True

        # Bottom
        isVisibleFromBottom = True
        for i in range(rowIndex + 1, len(trees)):
            if trees[i][columnIndex] >= treeHeight:
                isVisibleFromBottom = False
                break

        if isVisibleFromBottom:
            isVisible = True

        # Left
        isVisibleFromLeft = True
        for i in range(0, columnIndex):
            if trees[rowIndex][i] >= treeHeight:
                isVisibleFromLeft = False
                break

        if isVisibleFromLeft:
            isVisible = True

        # Right
        isVisibleFromRight = True
        for i in range(columnIndex + 1, len(trees[0])):
            if trees[rowIndex][i] >= treeHeight:
                isVisibleFromRight = False
                break

        if isVisibleFromRight:
            isVisible = True


        if isVisible:
            noOfVisibleTrees += 1


print(noOfVisibleTrees)
