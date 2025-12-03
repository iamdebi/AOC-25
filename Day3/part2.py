
# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day3/input"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day3/example"
f = open(inputName)

lineNumber = 1

sum = 0

for bank in f:
    print("---------------------")
    bank = bank.strip()              
    parsedBank = [int(battery) for battery in bank]

    highest = max(parsedBank)
    highestPos = parsedBank.index(highest)

    secondList = parsedBank[highestPos+1:]

    if secondList:
        secondHighest = max(secondList)
        secondHighestPos = highestPos + 1 + secondList.index(secondHighest)
    else:
        leftList = parsedBank[:highestPos]
        secondHighest = max(leftList)
        secondHighestPos = leftList.index(secondHighest)

    if highestPos < secondHighestPos:
        joltage = highest * 10 + secondHighest
    else:
        joltage = secondHighest * 10 + highest
    
    print(f"joltage: {joltage}")
    sum += joltage

print(f"total sum: {sum}")
f.close()