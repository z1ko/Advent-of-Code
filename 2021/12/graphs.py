
def add_or_create(childrens, parent, child):
    if parent in childrens:
        childrens[parent].append(child)
    else:
        childrens[parent] = [ child ]


def explore(node: str, childrens, explored_once, twice):
    
    # Abbiamo raggiunto la fine del percorso
    if node == 'end':
        return 1

    # Se siamo una grotta piccola
    small_caves = explored_once.copy()
    if node.islower():
        small_caves.add(node)

    result = 0
    if node in childrens:
        for child in childrens[node]:

            # Se non abbiamo mai visitato questa grotta piccola
            if child not in small_caves:
                result += explore(child, childrens, small_caves, twice)

            # Se l'abbiamo giò visitata ma non abbiamo già usato il jolly
            # allora la visitiamo cmq (tranne se è start)
            elif not twice and child != 'start':
                result += explore(child, childrens, small_caves, True)

    return result


# Contiene i figli di ogni nodo
childrens = { }
with open("2021/12/values") as f:
    
    for line in f.readlines():
        nodeA, nodeB = line.rstrip().split('-')

        add_or_create(childrens, nodeA, nodeB)
        add_or_create(childrens, nodeB, nodeA)


paths = explore("start", childrens, set(), False)
print(f"Numero di percorsi trovati: {paths}")