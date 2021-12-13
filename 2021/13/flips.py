
def flip(origin, value):
    if value > origin:
        return 2 * origin - value
    else:
        return value


def visualize(points):

    max_x = 1
    max_y = 1

    for x, y in points:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x,y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

    print('--------------------------------')


points = set()
flips  = []

with open("2021/13/values") as f:
    
    reading_points = True
    for line in f.readlines():
        if reading_points:

            if line != '\n':

                x, y = [ int(c) for c in line.rstrip().split(',') ]
                points.add((x,y))

            else:
                reading_points = False

        else:

            tokens = line.rstrip().split(' ')
            tokens = tokens[2].split('=')

            origin = int(tokens[1])
            axis   = tokens[0]

            flips.append((origin, axis))

print(f"Numero di punti all'inizio: { len(points) }")
for origin, axis in flips:

    new_points = set()
    for x, y in points:

        if axis == 'x':
            x = flip(origin, x)
        else:
            y = flip(origin, y)

        new_points.add((x, y))

    points = new_points
    print(f"Numero di punti: { len(points) }")

print(f"Numero di punti finali: { len(points) }")
visualize(points)