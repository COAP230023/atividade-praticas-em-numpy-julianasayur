# 33. Únicos + contagens + primeira ocorrência (médio)
# Para x = [3,1,2,3,2,3,1], obtenha valores únicos, contagens e índice da primeira
# ocorrência de cada valor.
import numpy as np
x = np.array([3,1,2,3,2,3,1])
valores, idx_primeira, contagens = np.unique(
x, return_index=True, return_counts=True
)
print("Valores únicos:", valores)
print("Contagens:", contagens)
print("Índice da primeira ocorrência:", idx_primeira)