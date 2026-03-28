# 27. np.where condicional (médio)
# Dado x = np.arange(-5,6), substitua negativos por 0 e mantenha não-negativos.
import numpy as np
x = np.arange(-5,6)
x = np.where(x < 0, 0, x)
print(x)