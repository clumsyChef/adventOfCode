data = open("input.txt", "r")

pointDict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "lost": 0,
    "draw": 3
}

refDict = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

anotherRefDict = {
    "rock": "X",
    "paper": "Y",
    "scissors": "Z",
    "X": "lost",
    "Y": "draw",
    "Z": "win"
}

def result(compInp, yourInp):
    moves = ["rock", "paper", "scissors"]
    oneShift = ["scissors", "rock", "paper"]
    yourRef = None
    if (yourInp == "draw"):
        yourRef = anotherRefDict[refDict[compInp]]
    elif (yourInp == "win"):
        compInd = oneShift.index(refDict[compInp])
        yourInd = moves[compInd]
        yourRef = anotherRefDict[yourInd]
    else:
        compInd = moves.index(refDict[compInp])
        yourInd = oneShift[compInd]
        yourRef = anotherRefDict[yourInd]

    return yourRef
        


def calculatePoints():
    totalPoints = 0
    for line in data.readlines():
        _line = line.replace("\n", "")
        _split = _line.split(" ",  1)
        comp, youNeedTo = _split[0], anotherRefDict[_split[1]]
        _result = result(comp, youNeedTo)
        totalPoints += (pointDict[_result] + pointDict[youNeedTo])

    return totalPoints
        

print(calculatePoints())
