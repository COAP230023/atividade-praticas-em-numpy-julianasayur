# 22. Centralizar colunas (fácil)
# Dada A = np.array([[1.,2.,3.],[4.,5.,6.]]), subtraia a média de cada coluna.
import numpy as np
A = np.array([[1., 2., 3.],
[4., 5., 6.]])
m = A.mean(axis=0)
A_centralizada = A - m
print("Médias:", m)
print("Resultado:\n", A_centralizada)