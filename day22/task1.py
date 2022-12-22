inputFile = open("input.txt", "r")

board = []

pathInstructions = []

parsingPhase = "Map"

for line in inputFile:
    if len(line) <= 1:
        parsingPhase = "Path"
        continue
    if parsingPhase == "Map":
        boardRow = list(line[:-1])
        if len(board) == 0:
            board.append(boardRow)
        else:
            while len(boardRow) < len(board[0]):
                boardRow.append(' ')
            board.append(boardRow)
    else:
        pathInstructionString = line[:-1]

inputFile.close()

numberString = ""
for character in pathInstructionString:
    if character.isdigit():
        numberString += character
    else:
        pathInstructions.append(int(numberString))
        numberString = ""
        pathInstructions.append(character)
pathInstructions.append(int(numberString))


# Find starting position
position = [0, len(board[0])]
direction = "E"

for i in range(len(board[0])):
    if board[0][i] == ".":
        if i < position[1]:
            position = [0, i]


directions = ["N", "E", "S", "W"]

# Follow the path
for pathInstruction in pathInstructions:
    
    if pathInstruction == "L":
        direction = directions[(directions.index(direction) + 3) % 4]
        
    elif pathInstruction == "R":
        direction = directions[(directions.index(direction) + 1) % 4]
        
    else:
        for i in range(pathInstruction):
            if direction == "N":
                if board[(position[0] - 1)%len(board)][position[1]] == ".":
                    position[0] -= 1
                elif board[(position[0] - 1)%len(board)][position[1]] == "#":
                    # Hit the wall
                    pass
                elif board[(position[0] - 1)%len(board)][position[1]] == " ":
                    newPositionCheck = [(position[0] - 1)%len(board), position[1]]
                    while board[newPositionCheck[0]][newPositionCheck[1]] == " ":
                        newPositionCheck[0] -= 1
                        newPositionCheck[0] %= len(board)
                    if board[newPositionCheck[0]][newPositionCheck[1]] == "#":
                        # Wall blocking
                        pass
                    elif board[newPositionCheck[0]][newPositionCheck[1]] == ".":
                        position[0] = newPositionCheck[0]
                        position[1] = newPositionCheck[1]

            elif direction == "E":
                if board[position[0]][(position[1] + 1)%len(board[0])] == ".":
                    position[1] += 1
                elif board[position[0]][(position[1] + 1)%len(board[0])] == "#":
                    # Hit the wall
                    pass
                elif board[position[0]][(position[1] + 1)%len(board[0])] == " ":
                    newPositionCheck = [position[0], (position[1] + 1)%len(board[0])]
                    while board[newPositionCheck[0]][newPositionCheck[1]] == " ":
                        newPositionCheck[1] += 1
                        newPositionCheck[1] %= len(board[0])
                    if board[newPositionCheck[0]][newPositionCheck[1]] == "#":
                        # Wall blocking
                        pass
                    elif board[newPositionCheck[0]][newPositionCheck[1]] == ".":
                        position[0] = newPositionCheck[0]
                        position[1] = newPositionCheck[1]

            elif direction == "S":
                if board[(position[0] + 1)%len(board)][position[1]] == ".":
                    position[0] += 1
                elif board[(position[0] + 1)%len(board)][position[1]] == "#":
                    # Hit the wall
                    pass
                elif board[(position[0] + 1)%len(board)][position[1]] == " ":
                    newPositionCheck = [(position[0] + 1)%len(board), position[1]]
                    while board[newPositionCheck[0]][newPositionCheck[1]] == " ":
                        newPositionCheck[0] += 1
                        newPositionCheck[0] %= len(board)
                    if board[newPositionCheck[0]][newPositionCheck[1]] == "#":
                        # Wall blocking
                        pass
                    elif board[newPositionCheck[0]][newPositionCheck[1]] == ".":
                        position[0] = newPositionCheck[0]
                        position[1] = newPositionCheck[1]

            elif direction == "W":
                if board[position[0]][(position[1] - 1)%len(board[0])] == ".":
                    position[1] -= 1
                elif board[position[0]][(position[1] - 1)%len(board[0])] == "#":
                    # Hit the wall
                    pass
                elif board[position[0]][(position[1] - 1)%len(board[0])] == " ":
                    newPositionCheck = [position[0], (position[1] - 1)%len(board[0])]
                    while board[newPositionCheck[0]][newPositionCheck[1]] == " ":
                        newPositionCheck[1] -= 1
                        newPositionCheck[1] %= len(board[0])
                    if board[newPositionCheck[0]][newPositionCheck[1]] == "#":
                        # Wall blocking
                        pass
                    elif board[newPositionCheck[0]][newPositionCheck[1]] == ".":
                        position[0] = newPositionCheck[0]
                        position[1] = newPositionCheck[1]

finalPassword = (position[0] + 1) * 1000 + (position[1] + 1) * 4
if direction == "N":
    finalPassword += 3
elif direction == "E":
    finalPassword += 0
elif direction == "S":
    finalPassword += 1
elif direction == "W":
    finalPassword += 2

print(finalPassword)
