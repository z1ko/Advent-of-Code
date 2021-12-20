
import math
from typing import Counter

class Node:
    def __init__(self, parent, left, right, value) -> None:

        self.parent = parent
        self.value  = value
        self.right  = right
        self.left   = left

    def __add__(self, other):

        result = Node(None, self, other, None)
        self.parent  = result
        other.parent = result

        return result 

    # La profondità è la distanza dalla radice
    def depth(self) -> int:
        result = 0

        curr = self
        while curr.parent != None:
            curr = curr.parent
            result += 1

        return result

    # Valore significativo di questo nodo
    def magnitude(self) -> int:
        
        if self.value != None:
            return self.value
        
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    # Splitta il nodo in due
    def split(self):
        assert(self.value != None)

        self.left  = Node(self, None, None, math.floor(self.value / 2))
        self.right = Node(self, None, None, math.ceil (self.value / 2))
        self.value = None


    def ascent_left(self):

        par = self.parent
        cur = self  

        while par != None and par.right == cur:

            cur = par
            par = cur.parent

        if par != None:
            return par
        else:
            return None


    def ascent_right(self):

        par = self.parent
        cur = self  

        while par != None and par.left == cur:

            cur = par
            par = cur.parent

        if par != None:
            return par
        else:
            return None

    def descent_left(self):

        cur = self
        while cur.left != None:
            cur = cur.left

        return cur

    def descent_right(self):

        cur = self
        while cur.right != None:
            cur = cur.right

        return cur
    

# ==================================================================

def visit(node):
    sequence = []
    previsit(node, sequence)
    return sequence

# Visita in profondità l'albero
def previsit(node, sequence):

    if node.left != None:
        previsit(node.left, sequence)

    sequence.append(node)

    if node.right != None:
        previsit(node.right, sequence)

def treestring(node):

    if node.value != None:
        return str(node.value)

    return f'[{treestring(node.left)},{treestring(node.right)}]' #({node.depth()})'


# Esplode un nodo
def explode(node):

    # Aggiunge valore a sinistra
    target = node.ascent_left()
    if target != None:
        target = target.right.descent_left()

        if target.value != None:
            target.value += node.right.value

    # Aggiunge valore a destra
    target = node.ascent_right()
    if target != None:
        target = target.left.descent_right()

        if target.value != None:
            target.value += node.left.value

    node.value = 0
    node.left  = None
    node.right = None

# Prova a ridurre
def reduce(node):

    while True:
        change = False
        
        # Se possiamo esplodere il nodo
        for node in visit(R):
            if node.depth() >= 4 and node.value == None:
                change = True

                print(f"Exploding \033[1;33m{treestring(node)}\033[m (depth = {node.depth()}) in \033[0;37m{treestring(R)}\033[m")
                explode(node)

        # Se possiamo dividere il nodo
        for node in visit(R):
            if node.value != None and node.value >= 10:
                change = True
                
                print(f"Splitting \033[1;33m{treestring(node)}\033[m in \033[0;37m{treestring(R)}\033[m")
                node.split()
                break

        # Usciamo dal ciclo
        if not change:
            break


# Data una riga dell'input ritorna il punto di divisione
def find_middle(line):

    count = 0
    for i, c in enumerate(line):
        if   c == '[': count += 1
        elif c == ']': count -= 1

        # Resistuisce indice della virgola dopo
        if count == 0:
            return i + 1

def generate_tree(line):
    
    if line.isnumeric():
        return Node(None, None, None, int(line))

    line = line[1:-1]
    middle = find_middle(line)
    return generate_tree(line[0:middle]) + generate_tree(line[middle + 1:])

PART1 = False

# Tutti gli alberi del file input
trees = []

R = Node(None, None, None, None)
with open("2021/18/values") as f:
    
    first = True
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        trees.append(line)

        T = generate_tree(line)
        if PART1:

            # Aggrega all'albero iniziale
            if not first:
                R = R + T
            else:     
                first = False
                R = T

            # Prova a ridurre
            reduce(R)

if PART1:
    print(f"Magnitudo di {treestring(R)}: {R.magnitude()}")

from itertools import product

maximum = 0
winner  = None

# Trova la combinazione che produce il valore più alto
for i in range(len(trees)):
    for j in range(len(trees)):
        if i != j:

            R = generate_tree(trees[i])
            reduce(R)
            
            T = generate_tree(trees[j])
            R = R + T
            reduce(R) 
            
            result = R.magnitude()
            if result > maximum:
                maximum = result
                winner = (i, j)
            
i, j = winner
A = generate_tree(trees[i])
B = generate_tree(trees[j])

print(f"La combinazione con magnitudo più alto: |{treestring(A)} + {treestring(B)}| = {maximum}")