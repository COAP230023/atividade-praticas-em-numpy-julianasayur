# 39. Convolução 2D (im2col) (difícil)
# Implemente convolução 2D &
# sliding_window_view para gerar blocos e multiplicação matricial.
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

I = np.arange(1, 17).reshape(4, 4) 
K = np.array([[1, 0],
[0, -1]])
H, W = I.shape
kH, kW = K.shape
blocks = sliding_window_view(I, (kH, kW)) 

cols = blocks.reshape(-1, kH * kW)
k_flat = K.reshape(-1)
out = cols @ k_flat 
out = out.reshape(H - kH + 1, W - kW + 1)
print("Imagem:")
print(I)
print("\nKernel:")
print(K)
print("\nConvolução 2D (valid):")
print(out)