import re
from collections import deque

# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day10/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day10/input"


def parse_line(line):
    # Indicator pattern inside [...]
    m = re.search(r"\[(.*?)\]", line)
    pattern = m.group(1)
    n = len(pattern)

    # Target bitmask
    target_mask = 0
    for i, ch in enumerate(pattern):
        if ch == "#":
            target_mask |= (1 << i)

    # Buttons: all (...) groups
    button_masks = []
    for group in re.findall(r"\((.*?)\)", line):
        group = group.strip()
        if not group:
            button_masks.append(0)
            continue
        bits = group.split(",")
        mask = 0
        for b in bits:
            idx = int(b)
            mask |= (1 << idx)
        button_masks.append(mask)

    return n, target_mask, button_masks


def min_presses_bfs(n_lights, target_mask, button_masks):
    # BFS over states 0..(2^n)-1
    start = 0
    if target_mask == start:
        return 0

    max_state = 1 << n_lights
    dist = [-1] * max_state

    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        state = q.popleft()
        d = dist[state]

        for bm in button_masks:
            next_state = state ^ bm

            if dist[next_state] == -1:
                dist[next_state] = d + 1
                if next_state == target_mask:
                    return d + 1
                q.append(next_state)

    # If unreachable (shouldn't happen with valid inputs)
    return None


total_presses = 0

with open(inputName) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        n, target_mask, button_masks = parse_line(line)
        presses = min_presses_bfs(n, target_mask, button_masks)
        # Optional: print per-machine result for debugging
        # print("Machine:", line)
        # print("  n =", n, "target =", bin(target_mask), "presses =", presses)
        total_presses += presses

print("Total minimum presses:", total_presses)
