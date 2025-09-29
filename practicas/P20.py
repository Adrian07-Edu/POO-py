tabla = [[x * y for x in range(1,11)] for y in range(1,11)]

print('|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10')
print('+---+---+---+---+---+---+---+---+---+---+---')
for fila in tabla:
    if fila[0] < 10: dato = ' |'
    else: dato = '|'
    print('| ', fila[0], dato, end='', sep='')
    for valor in fila:
        dato = ''
        if valor < 10: dato += '  '
        elif valor < 100: dato += ' '
        print(dato, valor, end=" ", sep='')
    print()

table = []
for y in range(11):
    table.append([])
    for x in range(11):
        if x == 0:
            table[x].append(y)

for row in table:
    print(row)