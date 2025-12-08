import math

# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day8/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day8/input"

points = []

with open(inputName) as f:
    for line in f:
        line = line.strip()
        x,y,z = line.split(",")
        points.append((int(x), int(y), int(z)))

pairs = []

for i in range(len(points)):
    x1, y1, z1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2, z2 = points[j]

        dist = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2 +
            (z2 - z1) ** 2 
        )

        pairs.append((dist, i, j))

pairs.sort()

parent = []
size = []

for i in range(len(points)):
    parent.append(i)
    size.append(1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return
    
    if size[rootA] < size[rootB]:
        parent[rootA] = rootB
        size[rootB]+= size[rootA]
    else:
        parent[rootB] = rootA
        size[rootA] += size[rootB]

limit = 1000
count = 0

for dist, a, b in pairs:
    if count == limit:
        break
    union(a, b)
    count +=1

circuits = {}

for i in range(len(points)):
    root = find(i)
    if root not in circuits:
        circuits[root] = 0
    circuits[root] += 1

size = list(circuits.values())
size.sort(reverse=True)

answer = size[0] * size[1] * size[2]

print(answer)
