# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day5/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day5/input"

f = open(inputName).read().split("\n\n")
    
ranges = f[0].split("\n")
ids = f[1].split("\n")

intervals = []

for r in ranges:
    if r == "":
        continue
    start, stop = r.split("-")
    intervals.append((int(start), int(stop)))

intervals.sort()

total = 0
cur_start, cur_end = intervals[0]

for start, end in intervals[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        total += (cur_end - cur_start + 1)
        cur_start, cur_end = start, end

total += (cur_end - cur_start + 1)


print(f"Ranges: {ranges}, {type(ranges)}")
print(f"Ids: {ids}, {type(ids)}")
print(f"Total: {total}, {type(total)}")
