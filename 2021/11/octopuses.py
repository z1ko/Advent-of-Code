
DAYS   = 100
CAVE_H = 10
CAVE_W = 10

# Ritorna l'indice di un polpo nell'array a partire dalle sue coordinate
def index(x, y):
    if x >= 0 and x < CAVE_W and y >= 0 and y < CAVE_H:
        return x + CAVE_W * y
    return None


# Ritorna le coordinate di un polpo a partire dal suo indice
def coord(i):
    if i >= 0 and i < CAVE_H * CAVE_W:
        return int(i % CAVE_W), int(i / CAVE_W)
    return None


# Visualizza caverna
def visualize(day, octopuses):

    print(f'----------------------------------------------- day: {day:<4}-----')
    for y in range(0, CAVE_H):
        for x in range(0, CAVE_W):
            print(f'{octopuses[index(x, y)]}', end = '')
        print('\n', end = '')


# Propaga il brillare dei polpi a tutti quelli vicini
def blink(ready, blinked, octopuses, octopus):

    x, y = coord(octopus)
    neighbors = [ 

        index(x + 1, y    ), index(x - 1, y    ), index(x    , y + 1), index(x    , y - 1), 
        index(x + 1, y + 1), index(x - 1, y + 1), index(x + 1, y - 1), index(x - 1, y - 1)    
    ]

    for neighbour in neighbors:
        if neighbour is not None:

            # Se non è un polpo che adnremo già a considerare
            if neighbour not in blinked and neighbour not in ready:
                octopuses[neighbour] += 1

                # Nuovo polpo da far brillare
                if octopuses[neighbour] > 9:
                    ready.append(neighbour)


# Fa brillare tutti i polpi pronti, ritorna il numero di blinks totali
def propagate(octopuses):

    ready   = []
    blinked = []
    
    # Trova polpi che possono brillare
    for i in range(0, len(octopuses)):
        octopuses[i] += 1

        if octopuses[i] > 9:
            ready.append(i)


    blinks = 0
    while len(ready) != 0:

        octopus = ready.pop()
        blink(ready, blinked, octopuses, octopus)
        blinked.append(octopus)

        blinks += 1

    # Resetta tutti i polpi che hanno blinkato
    for octopus in blinked:
        octopuses[octopus] = 0

    return blinks


octopuses = []
with open('2021/11/values') as f:

    for line in f.readlines():
        octopuses.extend([ int(c) for c in line.rstrip() ])

blinks = 0
day    = 0

while True:
    
    #visualize(day, octopuses)
    day_blinks = propagate(octopuses)
    blinks += day_blinks
    day += 1

    # Se tutti hanno blinkato
    if day_blinks == CAVE_W * CAVE_H:
        break

print(f"Blink dopo {day} giorni: {blinks}")