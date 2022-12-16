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


possibilities = [{ "currentValve" : "AA",
                   "openedValves" : [],
                   "totalFlow" : 0,
                   "flowRate" : 0}]

time = 30

while time > 0:

    print("Remaining time:", time)

    # Removing suboptimal possibilities

    newPossibilities = []
    
    if time > 20:
        for i in range(len(possibilities)):
            newPossibilities.append(possibilities[i])
        
    elif time > 15:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 3:
                newPossibilities.append(possibilities[i])

    else:
        maxFlowRate = 0
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate:
                maxFlowRate = possibilities[i]["flowRate"]
        for i in range(len(possibilities)):
            if possibilities[i]["flowRate"] > maxFlowRate // 3 * 2:
                newPossibilities.append(possibilities[i])
        
    possibilities = newPossibilities
    

    # Adding new possiblities
    
    newPossibilities = []

    for i in range(len(possibilities)):

        # Adding current flow rate to total flow
        possibilities[i]["totalFlow"] += possibilities[i]["flowRate"]
        
        currentValve = possibilities[i]["currentValve"]

        # Option 1 - open valve
        if currentValve not in possibilities[i]["openedValves"]:
            if valves[currentValve]["flowRate"] > 0:
                openedValves = possibilities[i]["openedValves"].copy()
                openedValves.append(currentValve)
                totalFlow = possibilities[i]["totalFlow"]
                flowRate = possibilities[i]["flowRate"] + valves[currentValve]["flowRate"]
                newPossibilities.append({ "currentValve" : currentValve,
                                          "openedValves" : openedValves,
                                          "totalFlow" : totalFlow,
                                          "flowRate" : flowRate })

        # Option 2 - move to another valve
        nextValves = valves[currentValve]["leadsTo"]
        for nextValve in nextValves:
            openedValves = possibilities[i]["openedValves"].copy()
            totalFlow = possibilities[i]["totalFlow"]
            flowRate = possibilities[i]["flowRate"]
            newPossibilities.append({ "currentValve" : nextValve,
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
