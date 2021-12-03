# 1) 1882980
# 2) 1971232560

class submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.pos   = 0
        self.aim   = 0

    def down(self, arg):
        self.aim += arg

    def up(self, arg):
        self.aim -= arg

    def forward(self, arg):
        self.depth += self.aim * arg
        self.pos += arg


with open('values') as f:
    lines = f.readlines()

sub = submarine()
for line in lines:
    tokens = line.split()

    # Invoca in modo dinamico la funzione associata
    getattr(sub, tokens[0])(int(tokens[1]))
      
print("Mul. finale: " + str(sub.depth * sub.pos))