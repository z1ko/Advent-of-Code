
# Questo è il display a 7 segmenti di riferimento
#
#  AAAA
# B    C
# B    C
#  DDDD
# E    F
# E    F
#  GGGG


display = {

    frozenset("ABCEFG")  : '0',
    frozenset("CF")      : '1',
    frozenset("ACDEG")   : '2',
    frozenset("ACDFG")   : '3',
    frozenset("BCDF")    : '4',
    frozenset("ABDFG")   : '5',
    frozenset("ABDEFG")  : '6',
    frozenset("ACF")     : '7',
    frozenset("ABCDEFG") : '8',
    frozenset("ABCDFG")  : '9' 
}


with open('2021/07/values') as f:

    total_sum = 0
    for line in f.readlines():
        sections = line.rstrip().split('|')

        resolver = { }
        redirect = { }

        # Ottiene valori di output
        digits = [ x for x in sections[0].split(' ') if x != '' ]
        for value in digits:

            # Prima analizziamo il mapping delle cifre univoche
            length = len(value)
            if   length == 2: resolver['CF']      = frozenset(value)
            elif length == 4: resolver['BCDF']    = frozenset(value)
            elif length == 3: resolver['ACF']     = frozenset(value)
            elif length == 7: resolver['ABCDEFG'] = frozenset(value)

        resolver['EG'] = resolver['ABCDEFG'] - resolver['BCDF'] - resolver['ACF']
        resolver['BD'] = resolver['BCDF'] - resolver['CF']

        # Le componenti minime che riusciamo a trovare all'inizio sono A, EG, BD e CF
        # con BD e EG riusciamo ad isolare il 5 e il 2 fra i 3 segnali di lunghezza 5 :)

        for value in [ frozenset(v) for v in digits if len(v) == 5 ]:
            
            if resolver['BD'] - value == frozenset():
                resolver['ABDFG'] = value
            elif resolver['EG'] - value == frozenset():
                resolver['ACDEG'] = value

        resolver['CE'] = resolver['ABCDEFG'] - resolver['ABDFG']
        resolver['BF'] = resolver['ABDFG'] - resolver['ACDEG']
        
        # Queste sono le soluzioni

        resolver['A'] = resolver['ACF'] - resolver['CF']
        resolver['E'] = resolver['CE' ] & resolver['EG']
        resolver['G'] = resolver['EG' ] - resolver['E' ]
        resolver['C'] = resolver['CE' ] - resolver['E' ]
        resolver['F'] = resolver['CF' ] - resolver['C' ]
        resolver['B'] = resolver['BF' ] - resolver['F' ]
        resolver['D'] = resolver['BD' ] - resolver['B' ]

        # Ora possiamo mappare ogni lettera al display di riferimento

        for segment in 'ABCDEFG':
            signal, = resolver[segment]
            redirect[signal] = segment

        display_result = ''
        output = [ x for x in sections[1].split(' ') if x != '' ]
        for string in output:
            
            corrected_signal = set()
            for signal in string:
                corrected_signal.add(redirect[signal])

            display_result += display[frozenset(corrected_signal)]


        print(f"Risultato display: {display_result}")
        total_sum += int(display_result)

    print(f"Somma totale: {total_sum}")

# Non mi piace molto come soluzione, ne ho viste di molto più geniali, ma cmq non mi lamento:
# ha il suo perchè :)