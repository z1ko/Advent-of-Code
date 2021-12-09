
def measure(table, point):
    x, y = point

    H = len(table)
    W = len(table[0])

    if x >= 0 and x < W and y >= 0 and y < H:
        return table[y][x]
    return None


def local_minimum(table, x, y):

    s = measure(table, (x, y))
    minimum = True

    points = [ (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) ]
    for point in points:
        m = measure(table, point)
        if m is not None and m <= s:
            minimum = False
            break

    return minimum, s


def basin_value(table, point):
    
    frontier = [ point ]
    visited  = []

    while len(frontier) != 0:
        
        point = frontier.pop(0)
        visited.append(point)
        x, y = point

        # punti vicini
        points = [ (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) ]
        for point in points:
            if point not in visited and point not in frontier:


                m = measure(table, point)
                if m is not None and m != 9:
                    frontier.append(point)

    return len(visited)



table = []
with open('2021/09/values') as f:
    for line in f.readlines():
        table.append([ int(c) for c in line.rstrip() ])


minimums = []
for y in range(0, len(table)):
    for x in range(0, len(table[0])):

        minimum, value = local_minimum(table, x, y)
        if minimum: minimums.append((x, y))


basins = []
for minimum in minimums:
    basins.append(basin_value(table, minimum))

basins = sorted(basins)
basins.reverse()

result = basins[0] * basins[1] * basins[2]
print(f"Risultato: {result}")