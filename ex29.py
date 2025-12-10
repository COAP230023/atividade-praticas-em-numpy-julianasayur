# 29. Produto cartesiano (broadcasting) (médio)
# Dado a=[1,2,3] e b=[10,20,30,40], gere todas as somas possíveis a_i + b_j via
# broadcasting (matriz 3×4).
import numpy as np
a = np.array([1,2,3])
b = np.array([10,20,30,40])
resultado = a[:, None] + b
print(resultado)