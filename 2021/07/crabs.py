
import statistics
import math

# Calcola punteggio della soluzione semplice
def cost_1(values, median):
    
    cost = 0
    for value in values:
        cost += int(abs(median - value))

    return cost


# Calcola punteggio della soluzione difficile
def cost_2(values, median):
    
    cost = 0
    for value in values:

        delta = int(abs(median - value))
        cost += delta * (delta + 1)

    return cost


# Trova il valore che minimizza la funzione di costo
def descent(values):

    # Partiamo dalla media, sembra una buona euristica
    target = statistics.mean(values)
    result = cost_2(values, target)

    steps = 1
    while True:

        l_cost = cost_2(values, target - 1)
        r_cost = cost_2(values, target + 1)

        sign  = math.copysign(1, l_cost - r_cost)
        delta = 1 # TODO: scegli delta dinamico

        # Trovato punto minimo della funzione
        if l_cost > result and r_cost > result:
            break

        # Prossimo step
        result = l_cost if l_cost < result else r_cost
        target = target + sign * delta
        steps += 1 
    
    return (int(target), result, steps)
        

# Beh, cerchiamo il punto più basso della funzione
with open('2021/07/values') as f:
    
    values = [ int(x) for x in f.readline().rstrip().split(',') ]

    # A quanto pare questo è un caso felice dove la media approssima incredibilmente bene il minimo
    # della funzione di costo, quindi tutto quello che ho fatto è in parte inutile...
    #
    # value, result, steps = descent(values)
    # 
    # delta = max(values) - min(values)
    # print(f'Costo minimo per il valore {value}: {result} (calcolato con {steps} steps, vantaggio: { 1.0 - steps / delta})')
    # 

    target = math.floor(statistics.mean(values))
    result = cost_2(values, target)

    print(f'costo minimo per input {target}: {result}')

