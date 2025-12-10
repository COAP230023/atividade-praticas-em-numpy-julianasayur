# 5. Índices não zero (fácil)
# Dado o vetor v = np.array([1,2,0,0,4,0]), encontre os índices dos elementos não nulos.
import numpy as np
v = np.array([1,2,0,0,4,0])
indices = np.nonzero(v)

print(indices)