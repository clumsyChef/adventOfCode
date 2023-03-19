def countCals():
    fileData = open("text-1.txt", "r")
    eachCalories = []
    total = 0
    for i in fileData.readlines():
        _line = i.replace("\n", "")
        if (len(_line)):
            numb = int(_line)
            total += numb
        else:
            eachCalories.append(total)
            total = 0

    eachCalories.append(total)
    return eachCalories


def top3CalsSum(calsArr):
    calsSorted = sorted(calsArr, reverse=True)
    top3 = calsSorted[0:3]
    print(top3)
    _summ = sum(top3)
    return _summ 

# Part 1
allCalsArr = countCals()
maxCals = max(allCalsArr)

# Part 2
max3Cals = top3CalsSum(allCalsArr)
print(max3Cals)
