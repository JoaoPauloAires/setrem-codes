import numpy as np
from scipy.stats import mode

mancha = np.array(['grande', 'pequena', 'grande', 'pequena', 'grande', 'grande'])

# Calcula a moda do array.
# Retorna a moda e quantidade de vezes correspondente.
moda, qtd = mode(mancha)

print(f'A moda é a categoria {moda}. Quantidade de vezes que ocorre: {qtd}')
