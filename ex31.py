# 31. Normalização min–max por coluna (médio)
# Dada A = rng.normal(size=(5,4)), normalize cada coluna para o intervalo [0,1], tratando colunas
# constantes.
import numpy as np
rng = np.random.default_rng(0)
A = rng.normal(size=(5,4))
col_min = A.min(axis=0)
col_max = A.max(axis=0)
range_ = col_max - col_min
range_safe = np.where(range_ == 0, 1, range_)
A_norm = (A - col_min) / range_safe
print("A original:\n", A)
print("\nNormalizada [0,1]:\n", A_norm)