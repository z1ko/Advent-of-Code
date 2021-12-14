
from collections import defaultdict, Counter

# Espande e ritorna la frequenza degli elementi
def expand(section, memory, step) -> Counter:

    # Calcola frequenza delle componenti della sezione
    if step == 0 or len(section) == 1:
        return Counter(section[0])

    saved = memory.get((section, step))
    if saved is None:

        derivation = transformations[section]
        l_res = expand(section[0] + derivation, memory, step - 1)
        r_res = expand(derivation + section[1], memory, step - 1)

        result = l_res + r_res
        memory[(section, step)] = result
        return result

    # Problema già affrontato
    print(f"Using cached solution for section {section} at step {step}")
    return saved


# Lista rappresentante il polimero
polymer = []

# Tutte le trasformazioni possibili
transformations = defaultdict(None)

with open("2021/14/values") as f:

    reading_polymer = True
    for line in f.readlines():
        if reading_polymer:

            if line == '\n':
                reading_polymer = False
                continue

            polymer = line.rstrip()

        else:
            root, _, derivation = line.rstrip().split(' ')
            transformations[root] = derivation


memory  = defaultdict(None)
counter = Counter()

ITERATIONS = 40
for i in range(0, len(polymer)):
    counter.update(expand(polymer[i : i + 2], memory, ITERATIONS))

ordered  = counter.most_common()
m_common = ordered[ 0]
l_common = ordered[-1]

print(f"Massima differenza trovata fra elementi: { m_common[1] - l_common[1] }")