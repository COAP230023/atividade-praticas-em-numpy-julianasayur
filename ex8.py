# 8. Aleatórios 3×3×3 (fácil)
# Gere um array 3×3×3 com valores aleatórios uniformes em [0,1). Use
# np.random.default_rng(42).
import numpy as np
rng = np.random.default_rng(42)
A = rng.random((3,3,3))
print(A)