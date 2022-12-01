import fileinput

caloriesByElf = [0]
elfIndex = 0

with fileinput.input() as lines:
    for line in lines:
        number = line[:-1]
        if len(number) == 0:
            caloriesByElf.append(0)
            elfIndex += 1
        else:
            caloriesByElf[elfIndex] += int(line)

print(max(caloriesByElf))
