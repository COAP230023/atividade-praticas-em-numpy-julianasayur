# 10. Padronização 1D (fácil)
# Dado x = [1,2,3,4,5], crie um array float e normalize para média 0 e desvio 1.
import numpy as np
x = np.array([1,2,3,4,5], dtype = float)
x_pad = (x - x.mean()) / x.std()
print(x_pad)