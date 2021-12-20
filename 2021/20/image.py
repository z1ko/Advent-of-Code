
from collections import defaultdict

INIT_W = 5
INIT_H = 5

M = {

    '.' : '0',
    '#' : '1'
}

PART1 = True

def sample(data, i, x, y):
    result = data.get((x, y))
    if result != None:
        return result
    
    # Trattiamo l'infinito!
    elif not PART1:
        if i % 2 == 0: return '.'
        else: return '#'

    else:
        return '.'


def kernel(data, i, x, y):
    seq = ""
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            seq += M[sample(data, i, x + dx, y + dy)]

    return int(seq, 2)

def visualize(data, i):

    BORDER = 5

    max_x = -1e9
    min_x =  1e9
    max_y = -1e9
    min_y =  1e9

    for (x, y) in data.keys():

        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    for y in range(min_y - BORDER, max_y + 1 + BORDER):
        if y == min_y - 1:
            print('\n', end='')

        for x in range(min_x - BORDER, max_x + 1 + BORDER):
            if x == min_x - 1:
                print(' ', end='')

            # Pixel acceso
            if sample(data, i, x, y) == '#':
                print(f'\033[1;35m#', end='')

            # Dati originali
            elif x >= 0 and x < INIT_W and y >= 0 and y < INIT_H:
                print(f'\033[0;37m{sample(data, i, x, y)}', end='')
            else:
                print(f'\033[1;30m{sample(data, i, x, y)}', end='')

            if x == max_x + 1:
                print(' ', end='')

        if y == max_x + 1:
            print('\n', end='')

        print('\n', end='')

    print('\033[m\n', end='')

data = defaultdict(None)
with open("2021/20/test") as f:

    # Soluzione da cui campionare
    solution = f.readline().rstrip()
    f.readline()

    for y in range(INIT_H):
        line = f.readline().rstrip()
        for x in range(INIT_W):
            data[(x, y)] = line[x]

ITER = 50
result = data
for i in range(ITER):
    visualize(result, i)

    saved = result.copy()

    delta = i + 1
    for y in range(-delta, INIT_H + delta):
        for x in range(-delta, INIT_W + delta):

            symbol = solution[kernel(saved, i, x, y)]
            result[(x, y)] = symbol

    

unos = 0
for val in result.values():
    if val == '#':
        unos += 1

visualize(result, i + 1)
print(f"Numero totale di pixel accesi: {unos}")