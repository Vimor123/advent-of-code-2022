inputFile = open("input.txt", "r")

inputString = inputFile.read()

inputFile.close()

for i in range(13, len(inputString) - 1):
    
    messageSet = set()
    
    for j in range(14):
        messageSet.add(inputString[i-j])
        
    if len(messageSet) == 14:
        print(i+1)
        break
