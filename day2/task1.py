inputFile = open("input.txt", "r")

games = []

for line in inputFile:
    games.append(line.split())

total = 0

for i in range(len(games)):
    
    if games[i][0] == "A":
        if games[i][1] == "X":
            total += 4
        elif games[i][1] == "Y":
            total += 8
        elif games[i][1] == "Z":
            total += 3

    elif games[i][0] == "B":
        if games[i][1] == "X":
            total += 1
        elif games[i][1] == "Y":
            total += 5
        elif games[i][1] == "Z":
            total += 9

    elif games[i][0] == "C":
        if games[i][1] == "X":
            total += 7
        elif games[i][1] == "Y":
            total += 2
        elif games[i][1] == "Z":
            total += 6

print(total)
