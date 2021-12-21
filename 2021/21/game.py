
import itertools

PLAYER_1_STARTING_POS = 3
PLAYER_2_STARTING_POS = 7

TABLE_SIZE = 10
WINNING_VALUE = 21

DP = { }

def limit(pos):
    return 1 + (pos - 1) % TABLE_SIZE

def explore(DP, pos1, score1, pos2, score2, turn):

    result = DP.get((pos1, score1, pos2, score2, turn))
    if result != None:
        return result

    if   score1 >= WINNING_VALUE: return (1, 0)
    elif score2 >= WINNING_VALUE: return (0, 1)

    # Primo giocatore
    results = []
    if turn % 2 == 0:
        # Per tutti i modi in cui si può sommare il dado
        for a, b, c in itertools.product([1, 2, 3], repeat = 3):

            roll = a + b + c
            position = limit(pos1 + roll)
            results.append(explore(DP, position, score1 + position, pos2, score2, turn + 1))
    
    # Secondo giocatore
    else:
        # Per tutti i modi in cui si può sommare il dado
        for a, b, c in itertools.product([1, 2, 3], repeat = 3):

            roll = a + b + c
            position = limit(pos2 + roll)
            results.append(explore(DP, pos1, score1, position, score2 + position, turn + 1))
    
    rw1 = 0
    rw2 = 0
    for (w1, w2) in results:
        rw1 += w1
        rw2 += w2

    result = (rw1, rw2)
    DP[(pos1, score1, pos2, score2, turn)] = result
    return result


result = explore(DP, PLAYER_1_STARTING_POS, 0, PLAYER_2_STARTING_POS, 0, 0)
print(f"Risultato: {result}")