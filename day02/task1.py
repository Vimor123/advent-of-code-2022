inputFile = open("input.txt", "r")

games = []

for line in inputFile:
    games.append(line.split())

inputFile.close()

scores = {
        "A": { "X": 4, "Y": 8, "Z": 3},
        "B": { "X": 1, "Y": 5, "Z": 9},
        "C": { "X": 7, "Y": 2, "Z": 6}
    }

total = 0

for i in range(len(games)):

    total += scores[games[i][0]][games[i][1]]

print(total)
