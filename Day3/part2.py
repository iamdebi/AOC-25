from typing import List, Tuple

# INPUT = "/Users/debbieurquhart/code_projects/AOC-25/Day4/example"
INPUT = "/Users/debbieurquhart/code_projects/AOC-25/Day4/input"

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def load_grid(path: str) -> List[List[str]]:
    with open(path, "r") as fh:
        rows = [line.rstrip("\n") for line in fh]
    return [list(row) for row in rows]

def is_roll(grid: List[List[str]], r: int, c: int) -> bool:
    if r < 0 or r >= len(grid):
        return False
    if c < 0 or c >= len(grid[r]):
        return False
    return grid[r][c] == "@"

def find_accessible(grid: List[List[str]]) -> List[Tuple[int,int]]:
    accessible = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != "@":
                continue
            neigh = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if is_roll(grid, nr, nc):
                    neigh += 1
            if neigh < 4:
                accessible.append((r, c))
    return accessible

def remove_rolls(grid: List[List[str]], coords: List[Tuple[int,int]]) -> int:
    for (r, c) in coords:
        grid[r][c] = "."
    return len(coords)

def annotate_grid(grid: List[List[str]], removed_coords: List[Tuple[int,int]]) -> List[str]:
    rows = []
    removed_set = set(removed_coords)
    for r in range(len(grid)):
        chars = []
        for c in range(len(grid[r])):
            if (r, c) in removed_set:
                chars.append("x")
            else:
                chars.append(grid[r][c])
        rows.append("".join(chars))
    return rows

def simulate_removal(path: str, verbose: bool = True) -> int:
    grid = load_grid(path)
    total_removed = 0
    round_no = 0

    if verbose:
        print("Initial grid:")
        for row in ["".join(r) for r in grid]:
            print(row)
        print()

    while True:
        accessible = find_accessible(grid)
        if not accessible:
            break
        round_no += 1
        removed = remove_rolls(grid, accessible)
        total_removed += removed

        if verbose:
            print(f"After round {round_no}, removed {removed} rolls (cumulative {total_removed}):")
            for row in ["".join(r) for r in grid]:
                print(row)
            print()

    if verbose:
        print(f"Stopped after {round_no} rounds. Total removed: {total_removed}")
    return total_removed

if __name__ == "__main__":
    total = simulate_removal(INPUT, verbose=True)
    print("TOTAL REMOVED:", total)
