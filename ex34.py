# 34. Matriz de distâncias 2D (médio)
# Dada P com N pontos 2D, compute a matriz NxN de distâncias euclidianas sem
# loops explícitos.
import numpy as np
def distancias(P):

    diff = P[:, None, :] - P[None, :, :] 
    D = np.sqrt(np.sum(diff**2, axis=2)) 
    return D