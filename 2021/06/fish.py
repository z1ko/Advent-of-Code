# Complessita O(Kg) dove g è il numero di giorni

# Propaga pesci nella lista
def cascade(fishes):
    result = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

    # Abbassa vita dei pesci
    for i in range(0, 8):
        result[i] = fishes[i + 1]

    # spawna nuovi pesci
    result[8]  = fishes[0]
    result[6] += fishes[0]

    return result


# Array contenente il numero di pesci per ogni stadio vitale
fishes = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

with open('2021/06/values') as f:
    initial = [ int(x) for x in f.readline().rstrip().split(',') ]
    
    for fish in initial:
        fishes[fish] += 1
    

# Simula per g giorni
for _ in range(0, 256):
    fishes = cascade(fishes)

# Conta i pesci
result = sum(fishes)
print(f'Numero totale di pesci dopo 80 giorni: {result}')