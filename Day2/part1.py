import math

inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day2/input1"

f = open(inputName).read()

rangesArray = f.split(",")
ids = []
totalSum = 0

for idRange in rangesArray:
    id1,id2 = idRange.split("-")
    # print(ids)
    ids.append((int(id1), int(id2)))

MAX_K = 12

for (id1, id2) in ids:

    for k in range(1, MAX_K + 1):

        M = 10**k + 1               
        AMin = 10**(k - 1)         
        AMax = 10**k - 1           
        
        ALow  = math.ceil(id1 / M)
        AHigh = math.floor(id2 / M)

        if ALow < AMin:
            ALow = AMin
        if AHigh > AMax:
            AHigh = AMax

        
        if ALow > AHigh:
            continue
        
        for A in range(ALow, AHigh + 1):
            N = A * M
            totalSum += N

print(totalSum)