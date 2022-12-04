inputFile = open("input.txt", "r")

groups = [[]]
groupMemberIndex = 0
groupIndex = 0

for line in inputFile:
    if groupMemberIndex >= 3:
        groupMemberIndex = 0
        groupIndex += 1
        groups.append([])
    groups[groupIndex].append(line[:-1])
    groupMemberIndex += 1

inputFile.close()

total = 0

for group in groups:
    for item in group[0]:
        if item in group[1]:
            if item in group[2]:
                if item.islower():
                    total += ord(item) - 96
                else:
                    total += ord(item) - 64 + 26
                break

print(total)
