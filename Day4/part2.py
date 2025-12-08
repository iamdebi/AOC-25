
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day4/input"
# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day4/example"
f = open(inputName)

lineNumber = 1

sum = 0

for bank in f:
    print("---------------------")
    bank = bank.strip()              
    
    batteriesOn = []
    remove = len(bank) - 12
    parsedBank = [int(battery) for battery in bank]

    for battery in parsedBank:
        while len(batteriesOn) > 0 and batteriesOn[-1] < battery and remove > 0:
            batteriesOn.pop(-1)
            remove -= 1
        batteriesOn.append(battery)

    while len(batteriesOn) > 12:
        batteriesOn.pop(-1)

    joltage = int("".join(str(battery) for battery in batteriesOn))

    sum += joltage

print(f"total sum: {sum}")
f.close()