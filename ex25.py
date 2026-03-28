# 25. Flatten vs. ravel (médio)
# Mostre a diferença entre flatten() (cópia) e ravel() (view quando possível). Modifique o
# resultado de ravel() e observe o original.
import numpy as np
A = np.array([[1, 2, 3],
[4, 5, 6]])
f = A.flatten()

r = A.ravel()
print("A original:\n", A)
print("\nflatten():", f)
print("\nravel(): ", r)
r[0] = 999
print("\nApós modificar ravel():")
print("ravel(): ", r)
print("A original modificada:\n", A)
print("flatten():", f) 