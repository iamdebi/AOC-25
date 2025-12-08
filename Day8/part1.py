# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day4/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day4/input"

with open(inputName, "r") as fh:
    grid = [line.rstrip("\n") for line in fh]

print("Loaded grid (rows, varying lengths allowed):")
for i, row in enumerate(grid):
    print(f"{i:2}: {row}")
print()

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

accessible_coords = []

def is_roll(r, c):
    if r < 0 or r >= len(grid):
        return False
    if c < 0 or c >= len(grid[r]):
        return False
    return grid[r][c] == "@"

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != "@":
            continue

        neighbor_count = 0
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if is_roll(nr, nc):
                neighbor_count += 1

        if neighbor_count < 4:
            accessible_coords.append((r, c))

annotated_rows = []
for r in range(len(grid)):
    row_chars = list(grid[r])
    for c in range(len(row_chars)):
        if (r, c) in accessible_coords:
            row_chars[c] = "x"
    annotated_rows.append("".join(row_chars))

print("Annotated grid (x = accessible):")
for row in annotated_rows:
    print(row)
print("---------------------------------------------------")
print("Accessible coordinates (r, c):", accessible_coords)
print("Total accessible rolls:", len(accessible_coords))
