# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day6/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day6/input"

f = open(inputName).read().split("\n\n")
    
ranges = f[0].split("\n")
ids = f[1].split("\n")

fresh = 0

for id in ids:
    if id == "":
        continue

    value = int(id)
    is_fresh = False

    for r in ranges:
        start, stop = r.split("-")
        start = int(start)
        stop = int(stop)

        if start <= value <= stop:
            is_fresh = True
            break

    if is_fresh:
        fresh += 1


print(f"Ranges: {ranges}, {type(ranges)}")
print(f"Ids: {ids}, {type(ids)}")
print(f"Fresh: {fresh}, {type(fresh)}")
