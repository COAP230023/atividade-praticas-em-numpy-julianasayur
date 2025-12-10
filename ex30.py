#30. Convolução 1D simples (médio)
#Implemente uma convolução 1D usando np.lib.stride_tricks.sliding_window_view
#sem usar np.convolve.


import numpy as np

x = np.array([1, 2, 3, 4, 5])
k = np.array([1, 0, -1])

jan = np.lib.stride_tricks.sliding_window_view(x, window_shape=len(k))

y = np.sum(jan * k[::-1], axis=1)

print("Sinal x:", x)
print("Kernel k:", k)
print("Resultado da convolução:", y)