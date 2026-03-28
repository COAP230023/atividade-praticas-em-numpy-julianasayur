# 24. Troca de colunas (fácil)
# Troque as colunas 0 e 2 de A = np.arange(12).reshape(3,4) sem copiar (sempre que
# possível).
import numpy as np
A = np.arange(12).reshape(3,4)
print("Antes:\n", A)
A[:, [0, 2]] = A[:, [2, 0]]
print("\nDepois:\n", A)