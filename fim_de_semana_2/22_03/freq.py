import numpy as np

mancha = np.array(['grande', 'pequena', 'grande', 'pequena', 'grande', 'grande'])

# Calcula a frequẽncia da categoria grande no atributo 'mancha'
freq = (mancha == 'grande').sum() / float(mancha.size)

print(f'Frequência da categoria "grande" é: {freq}')
