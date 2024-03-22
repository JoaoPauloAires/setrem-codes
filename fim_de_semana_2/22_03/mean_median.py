import numpy as np

idade = np.array([23, 20, 22, 21, 110])

# Calcula a média do array.
media = idade.mean()

# Calcula a mediana do array.
mediana = np.median(idade)

print(f"A média das idades é {media} e a mediana é: {mediana}")
