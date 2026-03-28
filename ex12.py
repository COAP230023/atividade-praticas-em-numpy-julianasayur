# 12. Clipping (fácil)
# Dado a = [2, 5, 7, 1, 9], limite os valores ao intervalo [0,5] (valores acima de 5 tornam-
# se 5).
import numpy as np
a = np.array([2,5,7,1,9])
a = np.clip(a, 0, 5)
print(a)