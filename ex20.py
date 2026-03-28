# 20. Lista de listas → array (fácil)
# Converta [[1,2,3],[4,5,6]] em ndarray, verifique shape e dtype.
import numpy as np
import numpy as np
lista = [[1,2,3],[4,5,6]]
A = np.array(lista)
print(A)
print("shape:", A.shape)
print("dtype:", A.dtype)