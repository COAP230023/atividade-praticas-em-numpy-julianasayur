# 26. Tabuleiro 8×8 (médio)
# Crie uma matriz 8×8 com padrão de tabuleiro (0 e 1 alternados).
import numpy as np
tab = (np.indices((8,8).sum(axis=0)) % 2
print(tab)