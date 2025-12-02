inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day1/input1"

current = 50
part2 = 0   # count any click that lands on 0 (part 2)

with open(inputName) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        steps = int(line[1:])


# If you want part2 you need to re-run and simulate counts of clicks:
current = 50
with open(inputName) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        steps = int(line[1:])
        d = 1 if direction == "R" else -1

        # compute first positive k where the dial hits 0
        k0 = (-current * d) % 100
        if k0 == 0:
            k0 = 100

        if steps >= k0:
            hits = 1 + (steps - k0) // 100
        else:
            hits = 0

        part2 += hits

        # update position after the whole rotation
        current = (current + d * steps) % 100

print("Part 2 (every click zeros):", part2)
