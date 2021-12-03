
# 1 2 3 4 5 6
# 
# A A A
#   B B B
#     C C C
#       D D D

def measure(values, idx) -> int:
    return values[idx] + values[idx + 1] + values[ idx + 2]

increments = 0
with open('values') as f:
    lines = f.readlines()

values = [ int(line) for line in lines ]
for i in range(0, len(values) - 3):
    if measure(values, i) < measure(values, i + 1):
        increments += 1
    
print("Incrementi: " + str(increments))