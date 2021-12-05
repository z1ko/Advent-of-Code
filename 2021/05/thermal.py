
from math import copysign

def add_or_set(points, value, incr, default):
    if value not in points:
        points[value] = default
    else:
        points[value] += incr

# Visualizza linee
def visualize(points):

    max_x = 0
    max_y = 0

    for key in points.keys():
        max_x = max(max_x, key[0])
        max_y = max(max_y, key[1])

    table = []
    for _ in range(0, max_y + 1):
        table.append([ 0 for i in range(0, max_x + 1) ])

    for key, value in points.items():
        table[key[1]][key[0]] = value

    print('\n')
    for row in table:
        for value in row:
            if value != 0:
                print(value, end='')
            else:
                print('.', end='')

        print(' ')


# Aggiunget tutti i punti di una linea
def integrate_add(points, beg, end):

    add_or_set(points, beg, 1, 1)

    step_x = 0
    step_y = 0

    delta_x = end[0] - beg[0]
    if delta_x != 0:
        step_x = int(copysign(1, delta_x))

    delta_y = end[1] - beg[1]
    if delta_y != 0:
        step_y = int(copysign(1, delta_y))
            
    runner = beg
    while runner[0] != end[0] or runner[1] != end[1]:
        runner = runner[0] + step_x, runner[1] + step_y
        add_or_set(points, runner, 1, 1)



points = {}
with open('2021/05/values') as f:
    lines = f.readlines()

    for line in lines:
        tokens = line.rstrip().split(' ')

        # beg: (x,y) -> end: (x, y)
        beg = tuple([ int(v) for v in tokens[0].split(',') ])
        end = tuple([ int(v) for v in tokens[2].split(',') ])

        integrate_add(points, beg, end)


#visualize(points)

# Calcola numero di punti con valore superiore a 1

count = 0
for value in points.values():
    if value > 1:
        count += 1

print(f"Numero di punti critici: {count}")