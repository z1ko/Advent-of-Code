

lines = []
with open('03/values') as f:
    lines = f.readlines()

def calcfreq(lines):
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in lines:

        # Conta il numero di uni per colonna
        for i in range(0, 12):
            if line[i] == '1':
                freq[i] += 1

    return freq

# Data una serie di numeri ritorna il bit più presente nella i-esima colonna,
# in caso di parità ritorna quello specificato
def most_frequent_bit(numbers, digit, tie):
        
    unos = 0
    for number in numbers:
        if number[digit] == '1':
            unos += 1

    breaker = len(numbers) / 2
    if unos == breaker:
        return (tie, True)

    if unos > breaker: 
        return ('1', False)
    else: 
        return ('0', False)

def invert_bit(bit):
    if bit == '1': return '0'
    if bit == '0': return '1'

# Data una serie di numeri trovato quello che ha progressivamente sempre le cifre più presenti 
def find(numbers, digits, tie, invert):

    result = numbers
    for i in range(0, digits):

        if len(result) == 1:
            return result[0]

        (winner_bit, is_tie) = most_frequent_bit(result, i, tie)
        if invert and not is_tie:
            winner_bit = invert_bit(winner_bit)

        result = [ n for n in result if n[i] == winner_bit]

    return result[0]

gamma   = 0
epsilon = 0

freq = calcfreq(lines)
for i in range(0, 12):
    bit = int(freq[i] > len(lines) / 2)

    gamma   = (gamma   << 1) | bit
    epsilon = (epsilon << 1) | (not bit)

print(f"gamma: {gamma:b}, epsilon: {epsilon:b}, result: {gamma * epsilon}")

oxygen = int(find(lines, 12, '1', False))
carbon = int(find(lines, 12, '0', True ))
result = oxygen * carbon

print(f"oxygen: {oxygen}, carbon: {carbon}, result: {result}")