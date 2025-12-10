# 32. Ordenar por coluna (médio)
# Ordene as linhas de A = np.array([[3,9],[1,4],[2,5]]) pelo valor crescente da 2ª coluna.
import numpy as np
A = np.array([[3,9],
[1,4],
[2,5]])
idx = np.argsort(A[:, 1])
A_ordenado = A[idx]
print(A_ordenado)