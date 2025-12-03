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


# Part 2 – Explanation

# An ID is invalid if it is made by taking a block of digits X and repeating it
# at least twice. For example:

#     55            -> "5" repeated 2 times
#     123123123     -> "123" repeated 3 times
#     1212121212    -> "12" repeated 5 times
#     1111111       -> "1" repeated 7 times

# To find these efficiently, we treat each invalid ID as:

#         N = X repeated R times
#         where:
#             X has d digits
#             R >= 2
#             total_digits = d * R

# We avoid constructing strings and instead build a numeric “mask”:

#         mask = 1 + 10^d + 10^(2d) + ... + 10^((R−1)d)

# Then:

#         N = X * mask

# For each input range (low, high):

# 1. Loop over all possible block sizes d (1 through 12).
# 2. Loop over all possible repeat counts R >= 2.
#    Stop increasing R when d * R exceeds the maximum number of digits (12).

# 3. Compute mask for (d, R).

# 4. Compute the range of possible X values by dividing the numeric range:

#         A_low  = ceil(low  / mask)
#         A_high = floor(high / mask)

# 5. Clamp X so it always has exactly d digits:

#         X_min = 10^(d-1)
#         X_max = 10^d - 1

# 6. For each valid X:
#         N = X * mask

#    We keep N only if:
#         - N has exactly d * R digits
#         - low <= N <= high

# 7. Important:
#    The same invalid ID can be produced by multiple (d, R) combinations.
#    Example: 111111 can be produced as:
#         d=1, R=6   (“1” × 6)
#         d=2, R=3   (“11” × 3)
#         d=3, R=2   (“111” × 2)

#    To avoid counting the same ID multiple times, we use a set() called 'seen'.
#    We only add N to the total the first time we encounter it.

# This approach ensures:
#     - No brute force iteration through entire ranges
#     - No string-based repetition for generation
#     - No invalid leading-zero patterns
#     - No duplicate repeated-pattern numbers

# This matches the rules for Part 2 and produces the correct Advent of Code answer.

