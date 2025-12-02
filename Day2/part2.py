import math

inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day2/input"
f = open(inputName).read()

rangesArray = f.split(",")
ranges = []
for idRange in rangesArray:
    id1, id2 = idRange.split("-")
    ranges.append((int(id1), int(id2)))

MAX_DIGITS = 12
seen = set()
total = 0

for (low, high) in ranges:

    for d in range(1, MAX_DIGITS + 1):        
        X_min = 10**(d - 1)                   
        X_max = 10**d - 1                     

        for R in range(2, MAX_DIGITS + 1):
            total_digits = d * R
            if total_digits > MAX_DIGITS:
                break

            
            mask = 0
            for i in range(R):
                mask += 10**(i * d)

            A_low  = math.ceil(low  / mask)
            A_high = math.floor(high / mask)

            if A_low < X_min:
                A_low = X_min
            if A_high > X_max:
                A_high = X_max
            if A_low > A_high:
                continue

            for X in range(A_low, A_high + 1):
                N = X * mask

                if len(str(N)) != total_digits:
                    continue

                if low <= N <= high:
                    if N not in seen:  
                        seen.add(N)
                        total += N

print(total)
