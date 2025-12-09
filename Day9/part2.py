inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/example"
# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/input"

points = []

with open(inputName) as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        x, y = line.split(",")
        points.append((int(x), int(y)))

maxArea = 0

red = set(points)
green = set()

def isBoundary(x, y):
    return (x, y) in red or (x, y) in green

for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]

    if x1 == x2:
        direction =  1 if y2 > y1 else -1
        for y in range(y1 + direction, y2, direction):
            green.add((x1, y))
    else:
        direction =  1 if x2 > x1 else -1
        for x in range(x1 + direction, x2, direction):
            green.add((x, y1))

min_x = min(x for x, y in points)
max_x = max(x for x, y in points)
min_y = min(y for x, y in points)
max_y = max(y for x, y in points)

visited = set()
stack = [(min_x, min_y)]

while stack:
    x, y = stack.pop()
    if (x, y) in visited:
        continue
    if isBoundary(x, y):
        continue

    visited.add((x, y))

    if x > min_x : stack.append((x-1, y))
    if x < max_x : stack.append((x+1, y))
    if y > min_y : stack.append((x, y-1))
    if y < max_y : stack.append((x, y+1))

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) not in visited and (x, y) not in red:
            green.add((x, y))

for i in range(len(points)):
    x1, y1 = points[i]

    for j in range(i + 1, len(points)):
        x2, y2 = points[j]

        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2)
        bottom = max(y1, y2)

        allowed = red | green

        valid = (
            (left, top) in allowed and
            (right, top) in allowed and
            (left, bottom) in allowed and
            (right, bottom) in allowed
        )

        if valid:
            width = right - left + 1
            height = bottom - top + 1
            area = width * height

            if area > maxArea:
                maxArea = area

print("Largest area:", maxArea)
