
from collections import defaultdict
import queue

BASE_MAP_W = 100
BASE_MAP_H = 100
BASE_MAP_S = 1

REAL_MAP_W = BASE_MAP_W * BASE_MAP_S
REAL_MAP_H = BASE_MAP_H * BASE_MAP_S

# Printa tabella
def visualize(table, solution):
    
    for y in range(REAL_MAP_H):
        for x in range(REAL_MAP_W):

            value = sample(table, x, y)
            if state(x, y) in solution: 
                print(f'\033[1;33m{value}', end = '')
            else:
                if x in range(BASE_MAP_W) and y in range(BASE_MAP_H):
                    print(f'\033[1;35m{value}', end = '')
                else:    
                    print(f'\033[1;30m{value}', end = '')                       

        print('\n', end = '')
    print('\033[0m')


# Ottiene il valore dalla mappa virtuale
def sample(map, x, y):
    
    # Ottiene la cella virtuale
    cell_x = x // BASE_MAP_W
    cell_y = y // BASE_MAP_H 

    value = map[(x % BASE_MAP_W) + (y % BASE_MAP_H) * BASE_MAP_W] + cell_x + cell_y
    while value > 9: value = value - 9

    return value

    
# Ottiene lo stato da una posizione
def state(x, y):
    return x + y * REAL_MAP_W


# Ottiene posizione di uno stato
def coords(state):
    return (state % REAL_MAP_W, state // REAL_MAP_H)


# Indica se una cella è interna alla mappa
def inside(x, y):
    return x in range(REAL_MAP_W) and y in range(REAL_MAP_H)


# Ottiene celle figlie
def neighbours(x, y):
    result = [ (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1) ]
    return [ (x, y) for (x, y) in result if inside(x, y) ]


# Ricerca del percorso migliore
def uniform_cost_search(map, source, target):

    Q = queue.PriorityQueue()
    Q.put((0, source, []))

    # Celle già visitate
    V = defaultdict(lambda: False)

    # Cella padre migliore per ogni cella e costo comulativo del padre
    # P = defaultdict(None)
    # P[source] = None

    while not Q.empty():
        cost, current, path = Q.get()

        # Evitiamo di espandere nodi già estratti con costo minore
        if V[current]: continue

        # Abbiamo finito con l'esplorazione
        if current == target: 
            break

        # Ora lo abbiamo esplorato
        V[current] = True

        x, y = coords(current)
        for child_x, child_y in neighbours(x, y):

            # Aggiungiamo nuova cella figlia se non già esplorata
            child = state(child_x, child_y)
            if not V[child]:

                child_cost = cost + sample(map, child_x, child_y)
                Q.put((child_cost, child, path + [ child ]))
                # P[child] = current 

    return path


# =================================================================================

map = []
with open("2021/15/values") as f:
    for line in f.readlines():
        map.extend([ int(x) for x in line.rstrip() ])

source = 0
target = len(map) * BASE_MAP_S * BASE_MAP_S - 1

assert(coords(target) == (REAL_MAP_W - 1, REAL_MAP_H - 1))

solution = uniform_cost_search(map, source, target)
visualize(map, solution)

result = 0
for step in solution:

    x, y = coords(step)
    result += sample(map, x, y)

print(f"Soluzioen con costo minimo: {result}")