inputFile = open("input.txt", "r")

commandLines = []

for line in inputFile:
    commandLines.append(line[:-1])

inputFile.close()

fileSystem = { '/' : {}}

currentFolder = '/'

folderSizes = []


def findSizeOfDirectory(path):

    global fileSystem

    positioning = fileSystem['/']

    folderToPosition = path[1:]

    totalSize = 0

    if path != "/":

            folderName = ""

            for i in range(len(folderToPosition)):
                
                if folderToPosition[i] == '/':
                    positioning = positioning[folderName]
                    folderName = ""
                else:
                    folderName += folderToPosition[i]
                    

    for contentName in positioning:

        if "int" in str(type(positioning[contentName])):

            totalSize += positioning[contentName]

        else:

            totalSize += findSizeOfDirectory(path + contentName + '/')

    return totalSize

    

for commandLine in commandLines:
    if commandLine[0] == "$":
        
        if commandLine[2:].startswith('cd'):
            
            if commandLine[5:].startswith('/'):
                currentFolder = '/'
                
            elif commandLine[5:].startswith('.'):

                folderSize = findSizeOfDirectory(currentFolder)

                folderSizes.append(folderSize)

                newCurrentFolder = ''
                levels = currentFolder.count('/')
                levels -= 1
                for i in range(len(currentFolder)):
                    if currentFolder[i] == '/':
                        levels -= 1
                    newCurrentFolder += currentFolder[i]
                    if levels <= 0:
                        break

                currentFolder = newCurrentFolder

            else:
                currentFolder += commandLine[5:] + "/"
            
    else:

        positioning = fileSystem['/']

        folderToPosition = currentFolder[1:]

        folderName = ""

        if currentFolder != "/":

            for i in range(len(folderToPosition)):
                
                if folderToPosition[i] == '/':
                    positioning = positioning[folderName]
                    folderName = ""
                else:
                    folderName += folderToPosition[i]
                    

        if commandLine.startswith('dir '):

            newFolderName = commandLine[4:]

            positioning[newFolderName] = {}

        else:

            size, newFileName = map(str, commandLine.split())

            size = int(size)

            positioning[newFileName] = size


            
unusedSpace = 70000000 - findSizeOfDirectory('/')

sizeForDeletion = 30000000 - unusedSpace

minFolder = 0


for size in folderSizes:
    if size >= sizeForDeletion:
        if minFolder == 0 or minFolder > size:
            minFolder = size

print(minFolder)
