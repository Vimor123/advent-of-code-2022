inputFile = open("input.txt", "r")

games = []

for line in inputFile:
    games.append(line.split())

inputFile.close()

scores = {
        "A": { "X": 3, "Y": 4, "Z": 8},
        "B": { "X": 1, "Y": 5, "Z": 9},
        "C": { "X": 2, "Y": 6, "Z": 7}
    }

total = 0

for i in range(len(games)):

    total += scores[games[i][0]][games[i][1]]

print(total)
