# 23. Produto elemento-a-elemento vs. escalar (fácil)
# Dadas a=[1,2,3] e b=[4,5,6], calcule produto elemento a elemento e o produto escalar.
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

produto_elemento = a * b

produto_escalar = np.dot(a, b)

print("Produto elemento a elemento: ", produto_elemento)
print("Produto escalar : ", produto_escalar)