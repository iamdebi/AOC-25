from shapely.geometry import Polygon, box

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

# The red loop polygon
poly = Polygon(points)

maxArea = 0

N = len(points)

# ----------------------------------------------------------
# Try every pair of red tiles as opposite corners of a rectangle
# ----------------------------------------------------------
for i in range(N):
    x1, y1 = points[i]

    for j in range(i + 1, N):
        x2, y2 = points[j]

        # Red corners must form a valid rectangle, not a line
        if x1 == x2 or y1 == y2:
            continue

        left = min(x1, x2)
        right = max(x1, x2)
        bottom = min(y1, y2)
        top = max(y1, y2)

        # Shapely rectangle (continuous geometry)
        rect = box(left, bottom, right, top)

        # The rectangle must lie entirely inside the red+green region,
        # which is exactly the interior of the polygon + its boundary.
        if rect.within(poly) or rect.touches(poly):
            width = (right - left + 1)
            height = (top - bottom + 1)
            area = width * height

            if area > maxArea:
                maxArea = area

print("Largest area:", maxArea)
