import numpy as np
from scipy.stats import trim_mean

x = np.array([1, 2, 3, 4, 5])

# Eliminar 20% (0.2) dos valores em cada extremidade
media_podada = trim_mean(x, 0.2)

print(f'Média podada: {media_podada}')
