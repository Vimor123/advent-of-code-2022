inputFile = open("input.txt", "r")

gustsOfWind = inputFile.read()

inputFile.close()


currentHeight = -1

chamber = []

for i in range(3):
    chamber.append(["."] * 7)

windIndex = 0

for i in range(2022):

    currentRockHeight = currentHeight + 4
    currentRockX = 2

    if i % 5 == 0:
        # -
        while len(chamber) <= currentHeight + 4:
            chamber.append(["."] * 7)
            
        landed = False
        while not landed:
            wind = gustsOfWind[windIndex]
            windIndex += 1
            if windIndex >= len(gustsOfWind):
                windIndex = 0

            # Follow the wind
            if wind == ">":
                if currentRockX < 3:
                    if chamber[currentRockHeight][currentRockX + 4] == ".":
                        currentRockX += 1
            elif wind == "<":
                if currentRockX > 0:
                    if chamber[currentRockHeight][currentRockX - 1] == ".":
                        currentRockX -= 1

            # Obey gravity
            if (chamber[currentRockHeight-1][currentRockX] == "." and
                chamber[currentRockHeight-1][currentRockX + 1] == "." and
                chamber[currentRockHeight-1][currentRockX + 2] == "." and
                chamber[currentRockHeight-1][currentRockX + 3] == ".") and currentRockHeight > 0:
                currentRockHeight -= 1
            else:
                landed = True
                chamber[currentRockHeight][currentRockX] = "#"
                chamber[currentRockHeight][currentRockX + 1] = "#"
                chamber[currentRockHeight][currentRockX + 2] = "#"
                chamber[currentRockHeight][currentRockX + 3] = "#"

                if currentHeight < currentRockHeight:
                    currentHeight = currentRockHeight

    elif i % 5 == 1:
        # +
        while len(chamber) <= currentHeight + 6:
            chamber.append(["."] * 7)

        landed = False
        while not landed:
            wind = gustsOfWind[windIndex]
            windIndex += 1
            if windIndex >= len(gustsOfWind):
                windIndex = 0

            # Follow the wind
            if wind == ">":
                if currentRockX < 4:
                    if (chamber[currentRockHeight][currentRockX + 2] == "." and
                        chamber[currentRockHeight + 1][currentRockX + 3] == "." and
                        chamber[currentRockHeight + 2][currentRockX + 2] == "."):
                        currentRockX += 1
            elif wind == "<":
                if currentRockX > 0:
                    if (chamber[currentRockHeight][currentRockX] == "." and
                        chamber[currentRockHeight + 1][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 2][currentRockX] == "."):
                        currentRockX -= 1

            # Obey gravity
            if (chamber[currentRockHeight - 1][currentRockX + 1] == "." and
                chamber[currentRockHeight + 1 - 1][currentRockX] == "." and
                chamber[currentRockHeight + 1 - 1][currentRockX + 2] == ".") and currentRockHeight > 0:
                currentRockHeight -= 1
            else:
                landed = True
                chamber[currentRockHeight][currentRockX + 1] = "#"
                chamber[currentRockHeight + 1][currentRockX] = "#"
                chamber[currentRockHeight + 1][currentRockX + 1] = "#"
                chamber[currentRockHeight + 1][currentRockX + 2] = "#"
                chamber[currentRockHeight + 2][currentRockX + 1] = "#"

                if currentHeight < currentRockHeight + 2:
                    currentHeight = currentRockHeight + 2

    elif i % 5 == 2:
        # reverse L
        while len(chamber) <= currentHeight + 6:
            chamber.append(["."] * 7)

        landed = False

        while not landed:
            wind = gustsOfWind[windIndex]
            windIndex += 1
            if windIndex >= len(gustsOfWind):
                windIndex = 0

            # Follow the wind
            if wind == ">":
                if currentRockX < 4:
                    if (chamber[currentRockHeight][currentRockX + 3] == "." and
                        chamber[currentRockHeight + 1][currentRockX + 3] == "." and
                        chamber[currentRockHeight + 2][currentRockX + 3] == "."):
                        currentRockX += 1
            elif wind == "<":
                if currentRockX > 0:
                    if (chamber[currentRockHeight][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 1][currentRockX + 1] == "." and
                        chamber[currentRockHeight + 2][currentRockX + 1] == "."):
                        currentRockX -= 1

            # Obey gravity
            if (chamber[currentRockHeight - 1][currentRockX] == "." and
                chamber[currentRockHeight - 1][currentRockX + 1] == "." and
                chamber[currentRockHeight - 1][currentRockX + 2] == ".") and currentRockHeight > 0:
                currentRockHeight -= 1
            else:
                landed = True
                chamber[currentRockHeight][currentRockX] = "#"
                chamber[currentRockHeight][currentRockX + 1] = "#"
                chamber[currentRockHeight][currentRockX + 2] = "#"
                chamber[currentRockHeight + 1][currentRockX + 2] = "#"
                chamber[currentRockHeight + 2][currentRockX + 2] = "#"

                if currentHeight < currentRockHeight + 2:
                    currentHeight = currentRockHeight + 2
                    

    elif i % 5 == 3:
        # I
        while len(chamber) <= currentHeight + 7:
            chamber.append(["."] * 7)

        landed = False

        while not landed:
            wind = gustsOfWind[windIndex]
            windIndex += 1
            if windIndex >= len(gustsOfWind):
                windIndex = 0

            # Follow the wind
            if wind == ">":
                if currentRockX < 6:
                    if (chamber[currentRockHeight][currentRockX + 1] == "." and
                        chamber[currentRockHeight + 1][currentRockX + 1] == "." and
                        chamber[currentRockHeight + 2][currentRockX + 1] == "." and
                        chamber[currentRockHeight + 3][currentRockX + 1] == "."):
                        currentRockX += 1
            elif wind == "<":
                if currentRockX > 0:
                    if (chamber[currentRockHeight][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 1][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 2][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 3][currentRockX - 1] == "."):
                        currentRockX -= 1

            # Obey gravity
            if chamber[currentRockHeight - 1][currentRockX] == "." and currentRockHeight > 0:
                currentRockHeight -= 1
            else:
                landed = True
                chamber[currentRockHeight][currentRockX] = "#"
                chamber[currentRockHeight + 1][currentRockX] = "#"
                chamber[currentRockHeight + 2][currentRockX] = "#"
                chamber[currentRockHeight + 3][currentRockX] = "#"

                if currentHeight < currentRockHeight + 3:
                    currentHeight = currentRockHeight + 3
                    

    elif i % 5 == 4:
        # Square
        while len(chamber) <= currentHeight + 5:
            chamber.append(["."] * 7)

        landed = False
        
        while not landed:
            wind = gustsOfWind[windIndex]
            windIndex += 1
            if windIndex >= len(gustsOfWind):
                windIndex = 0

            # Follow the wind
            if wind == ">":
                if currentRockX < 5:
                    if (chamber[currentRockHeight][currentRockX + 2] == "." and
                        chamber[currentRockHeight + 1][currentRockX + 2] == "."):
                        currentRockX += 1
            elif wind == "<":
                if currentRockX > 0:
                    if (chamber[currentRockHeight][currentRockX - 1] == "." and
                        chamber[currentRockHeight + 1][currentRockX - 1] == "."):
                        currentRockX -= 1

            # Obey gravity
            if (chamber[currentRockHeight - 1][currentRockX] == "." and
                chamber[currentRockHeight - 1][currentRockX + 1] == "." and currentRockHeight > 0):
                currentRockHeight -= 1
            else:
                landed = True
                chamber[currentRockHeight][currentRockX] = "#"
                chamber[currentRockHeight + 1][currentRockX] = "#"
                chamber[currentRockHeight][currentRockX + 1] = "#"
                chamber[currentRockHeight + 1][currentRockX + 1] = "#"

                if currentHeight < currentRockHeight + 1:
                    currentHeight = currentRockHeight + 1

print(currentHeight + 1)
