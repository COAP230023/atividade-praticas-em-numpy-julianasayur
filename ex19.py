# 19. Máscara booleana (fácil)
# Crie uma máscara para números pares de 0…19 e use-a para filtrar o
# vetor.
import numpy as np
v = np.arange(20)
pares = v[ v % 2 == 0]
print(pares)