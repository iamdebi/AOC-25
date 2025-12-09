# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/input"

points = []

with open(inputName) as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        x, y = line.split(",")
        points.append((int(x), int(y)))

maxArea = 0

for i in range(len(points)):
    x1, y1 = points[i]

    for j in range(i + 1, len(points)):
        x2, y2 = points[j]

        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1

        area = width * height

        if area > maxArea:
            maxArea = area

print("Largest area:", maxArea)
