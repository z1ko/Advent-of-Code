
import statistics

CLOSURES = [ '>', ')', ']', '}' ]
OPENINGS = [ '<', '(', '[', '{' ]

CLOSURE_OF = {

    '<' : '>',
    '(' : ')',
    '[' : ']',
    '{' : '}'
}

CORRUPTION_SCORE_OF = {
    
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}

AUTOCOMPLETE_SCORE_OF = {

    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

# Basta usare uno stack ed eliminare dalla cima tutti i chunk...
def corruption(string):

    stack = [ string[0] ]
    for i in range(1, len(string)):
        
        cur_symbol = string[i]
        if len(stack) != 0:
            top_symbol = stack.pop()
            
            if cur_symbol in CLOSURES:
                
                # Se non possiamo abbiamo trovato una corruzione
                if CLOSURE_OF[top_symbol] != cur_symbol:
                    return True, top_symbol, cur_symbol, None

                # Abbiamo risolto il chunck
                continue

            stack.append(top_symbol)
        stack.append(cur_symbol)

    result = 0
    for symbol in reversed(stack):
        #print(f'{CLOSURE_OF[symbol]}', end = '')
        result = result * 5 + AUTOCOMPLETE_SCORE_OF[symbol]
    #print('\n')

    # Nessuna corruzione
    return False, None, None, result


with open('2021/10/values') as f:
    
    corruption_score    = 0
    autocomplete_scores = []

    for line in f.readlines():
        line = line.rstrip()

        corrupted, begin, found, result = corruption(line)
        if corrupted:

            score = CORRUPTION_SCORE_OF[found]
            print(f"{line:>70} | Atteso '{CLOSURE_OF[begin]}' ma trovato '{found}', corruzione: {score}")
            corruption_score += score
        
        else:

            autocomplete_scores.append(result)
            print(f"{line:>70} | Valida con risultato di autocompletamento: {result}")


    autocomplete_score = statistics.median(autocomplete_scores)
    print(f"Risultato finale corruzione: {corruption_score}, autocompletamento: {autocomplete_score}")
