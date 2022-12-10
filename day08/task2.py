inputFile = open("input.txt", "r")

trees = []

for line in inputFile:
    numbers = line[:-1]
    treeHeights = []
    for digit in numbers:
        treeHeights.append(int(digit))
    trees.append(treeHeights)

inputFile.close()


maxScenicScore = 0

for rowIndex in range(1, len(trees) - 1):

    for columnIndex in range(1, len(trees[0]) - 1):

        treeHeight = trees[rowIndex][columnIndex]

        scenicScore = 1
        
        # Top
        visibleTreesFromTop = 0
        for i in range(rowIndex-1, -1, -1):
            visibleTreesFromTop += 1
            if trees[i][columnIndex] >= treeHeight:
                break

        scenicScore *= visibleTreesFromTop

        # Bottom
        visibleTreesFromBottom = 0
        for i in range(rowIndex + 1, len(trees)):
            visibleTreesFromBottom += 1
            if trees[i][columnIndex] >= treeHeight:
                break

        scenicScore *= visibleTreesFromBottom

        # Left
        visibleTreesFromLeft = 0
        for i in range(columnIndex-1, -1, -1):
            visibleTreesFromLeft += 1
            if trees[rowIndex][i] >= treeHeight:
                break

        scenicScore *= visibleTreesFromLeft

        # Right
        visibleTreesFromRight = 0
        for i in range(columnIndex + 1, len(trees[0])):
            visibleTreesFromRight += 1
            if trees[rowIndex][i] >= treeHeight:
                break

        scenicScore *= visibleTreesFromRight


        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore


print(maxScenicScore)
