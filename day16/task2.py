inputFile = open("input.txt", "r")

valves = {}

for line in inputFile:
    valveString, tunnelsString = map(str, line[:-1].split('; '))

    valve = valveString[6:8]
    flowRate = int(valveString[23:])

    if tunnelsString[21] == "s":
        tunnels = tunnelsString[23:].split(', ')
    else:
        tunnels = [tunnelsString[22:]]

    valves[valve] = { "flowRate" : flowRate,
                      "leadsTo" : tunnels }

inputFile.close()


possibilities = [{ "currentValves" : ["AA", "AA"],
                   "openedValves" : [],
                   "totalFlow" : 0,
                   "flowRate" : 0}]

time = 26

while time > 0:

    print("Remaining time:", time)

    # Removing suboptimal possibilities

    newPossibilities = []
    
    if time > 21:
        for i in range(len(possibilities)):
            newPossibilities.append(possibilities[i])
        
    elif time > 17:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 3:
                newPossibilities.append(possibilities[i])

    elif time > 15:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 3 * 2:
                newPossibilities.append(possibilities[i])

    elif time > 10:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 10 * 9:
                newPossibilities.append(possibilities[i])

    else:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 20 * 19:
                newPossibilities.append(possibilities[i])
        
    possibilities = newPossibilities
    

    # Adding new possiblities
    
    newPossibilities = []

    for i in range(len(possibilities)):

        # Adding current flow rate to total flow
        possibilities[i]["totalFlow"] += possibilities[i]["flowRate"]
        
        currentValves = possibilities[i]["currentValves"]

        currentValve1 = currentValves[0]
        currentValve2 = currentValves[1]

        openedValves = possibilities[i]["openedValves"]
        totalFlow = possibilities[i]["totalFlow"]
        flowRate = possibilities[i]["flowRate"]
        
        # Option 1 - both open valves
        if currentValve1 not in possibilities[i]["openedValves"] and currentValve2 not in possibilities[i]["openedValves"] and currentValve1 != currentValve2:
                
            if valves[currentValve1]["flowRate"] > 0 and valves[currentValve1]["flowRate"] > 0:

                openedValvesBoth = openedValves.copy()
                    
                openedValvesBoth.append(currentValve1)
                openedValvesBoth.append(currentValve2)

                newFlowRate = flowRate + valves[currentValve1]["flowRate"]
                newFlowRate += valves[currentValve2]["flowRate"]

                newPossibilities.append({ "currentValves" : currentValves,
                                          "openedValves" : openedValvesBoth,
                                          "totalFlow" : totalFlow,
                                          "flowRate" : newFlowRate })

        # Option 2 - 1 opens, 2 moves
        if currentValve1 not in possibilities[i]["openedValves"] and valves[currentValve1]["flowRate"] > 0:

            newOpenedValves = openedValves.copy()
            newOpenedValves.append(currentValve1)
            newFlowRate = flowRate + valves[currentValve1]["flowRate"]

            nextValves = valves[currentValve2]["leadsTo"]
            for nextValve in nextValves:
                newCurrentValves = [currentValve1, nextValve]
                newPossibilities.append({ "currentValves" : newCurrentValves,
                                          "openedValves" : newOpenedValves,
                                          "totalFlow" : totalFlow,
                                          "flowRate" : newFlowRate })

        # Option 3 - 1 moves, 2 opens
        if currentValve2 not in possibilities[i]["openedValves"] and valves[currentValve2]["flowRate"] > 0:

            newOpenedValves = openedValves.copy()
            newOpenedValves.append(currentValve2)
            newFlowRate = flowRate + valves[currentValve2]["flowRate"]

            nextValves = valves[currentValve1]["leadsTo"]
            for nextValve in nextValves:
                newCurrentValves = [nextValve, currentValve2]
                newPossibilities.append({ "currentValves" : newCurrentValves,
                                          "openedValves" : newOpenedValves,
                                          "totalFlow" : totalFlow,
                                          "flowRate" : newFlowRate })

        # Option 4 - both move
        nextValves1 = valves[currentValve1]["leadsTo"]
        nextValves2 = valves[currentValve2]["leadsTo"]

        for nextValve1 in nextValves1:
            for nextValve2 in nextValves2:
                newCurrentValves = [nextValve1, nextValve2]
                newPossibilities.append({ "currentValves" : newCurrentValves,
                                          "openedValves" : openedValves,
                                          "totalFlow" : totalFlow,
                                          "flowRate" : flowRate })

    possibilities = newPossibilities

    time -= 1


maxFlow = 0
for possibility in possibilities:
    if possibility["totalFlow"] > maxFlow:
        maxFlow = possibility["totalFlow"]

print("Max flow:", maxFlow)
