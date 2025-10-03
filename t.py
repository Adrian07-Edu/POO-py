carro = { 'Marca': 'ford', 'Modelo': 'focus', 'Color': 'Azul' }

for i in carro.keys(): print(i)
for i in carro.values(): print(i)
for k,v in carro.items(): print(k,'->',v)

let = carro.pop('Marca')
print(let)