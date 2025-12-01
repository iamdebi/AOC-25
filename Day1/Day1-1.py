
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day1/example"

f = open(inputName)
current = 50 
hit0 = 0

def is_over_99(currentPosition):
    if currentPosition > 99:
        amount = currentPosition - 99
        print(f"decreasing current by {amount}, currentPosition = {currentPosition}")
        currentPosition = 0 + amount - 1
        return currentPosition
    else:
        return currentPosition
    
def is_less_0(currentPosition):
    if currentPosition < 0:
        amount = 0 - currentPosition
        print(f"increasing current by {amount}, currentPosition = {currentPosition}")
        currentPosition = 99 - amount + 1
        return currentPosition
    else:
        return currentPosition

for line in f:
    direction = line[0]
    amount = int(line[1:])
    if direction == "L":
        current -= amount
        current = is_less_0(current)
    else:
        current += amount
        current = is_over_99(current)
        
    print(current)
    if current == 0:
        print("Hit 0")
        hit0 +=1

print(hit0)
f.close()