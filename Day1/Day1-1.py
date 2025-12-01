
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day1/input1"

f = open(inputName)
current = 50 
hit0 = 0
lineNumber = 1

def is_greater_than_99(pos):
    while pos > 99:
        pos = pos - 100
    return pos

def is_less_than_0(pos):
    while pos < 0:
        pos = pos + 100
    return pos

def is_more_than_100(amount):
    # This is equivalent to: amount % 100
    return amount % 100 
        

for line in f:
    print("---------------------")
    print(f"parsing line no {lineNumber}, contains: {line}")
    
    direction = line[0]
    toMove = int(line[1:])
    amount = 0
    if toMove > 100:
        print(f"greater than 100, to move {toMove}")
        amount = is_more_than_100(toMove)
        print(f"amount: {amount}")
    else:
        amount = toMove
        
    if direction == "L":
        print(f"current: {current}, amount: {amount}")
        newPos = current - amount
        newCur = is_less_than_0(newPos)
        print(f"newPos: {newPos}, newCur: {newCur}")
        current = newCur

    elif direction == "R":
        newPos = current + amount
        current = is_greater_than_99(newPos)

    if current == 0:
        hit0 +=1

    if current < 0:
        print(f"currentl has exceed 0, {lineNumber}:, {line}")
        break

    lineNumber +=1
    print(f"finished pasring line {line}, current: {current} of type {type(current)}")
    print("---------------------")

print(hit0)

# print(10 + -50) = -40


f.close()