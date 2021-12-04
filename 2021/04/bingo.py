

from typing import List

TABLE_SIZE = 5

class Table:
    def __init__(self, values) -> None:
        
        self.values    = values
        self.state     = {}
        self.positions = {}

        # Velocizza accesso alle celle per posizione e stato
        for i, value in enumerate(values):

            x = int(i % TABLE_SIZE)
            y = int(i / TABLE_SIZE)

            self.positions[value] = (x, y)
            self.state[value] = False

    # Accede ad un elemento in base alle sue coordinate
    def get_value_at_pos(self, x, y) -> bool:
        return self.values[x + y * TABLE_SIZE]

    # Aggiunge elemento e controlla se abbiamo vinto
    def check(self, value) -> bool:

        state = self.state.get(value)
        if state != None:

            # Aggiorna stato valore
            self.state[value] = True
            return self.winning(value)

        return False

    # Controlla se abbiamo vinto    
    def winning(self, value) -> bool:

        x, y = self.positions[value]

        # Orizzontale
        winning_oriz = True
        for i in range(0, TABLE_SIZE):
            inner_value = self.get_value_at_pos(i, y)
            if self.state[inner_value] == False:
                winning_oriz = False
                break

        # Verticale
        winning_vert = True
        for i in range(0, TABLE_SIZE):
            inner_value = self.get_value_at_pos(x, i)
            if self.state[inner_value] == False:
                winning_vert = False
                break

        return winning_oriz or winning_vert

    # Calcola risultato tabella
    def result(self, winner):

        sum = 0
        for value, state in self.state.items():
            if state == False:
                sum += value

        return sum * winner


# data una linea ritorna i valori presenti
def extract_values(line, separator):
    splitted = line.rstrip().split(separator)
    return [ int(x) for x in splitted if x.isdigit() ]

values = []
tables = []

with open('2021/04/test') as f:

    # Carica valori di gioco
    line = f.readline()
    values = extract_values(line, ',')

    lines = f.readlines()
    for i in range(0, len(lines), 6):
        
        table_lines = []
        for j in range(1, 6):
            table_lines += extract_values(lines[i + j], ' ')

        tables.append(Table(table_lines))

# Gioca
total_wins = 0
for value in values:

    for table in tables:
        if table.check(value) == True:

            print(f"{total_wins}) Winner with value {value}: {table.result(value)}\n")

            # Non sta più giocando
            tables.remove(table)
            total_wins += 1
