# 36. One-hot encoding (médio)
# Converta os rótulos y = [2,0,1,2] em codificação one-hot usando apenas operações
# NumPy.
import numpy as np
y = np.array([2, 0, 1, 2])

num_classes = y.max() + 1

one_hot = np.eye(num_classes)[y]
print(one_hot)