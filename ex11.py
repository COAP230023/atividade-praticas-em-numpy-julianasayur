# 11. Conversão de tipos (fácil)
# Converta np.array([1,2,3]) (int32) para float32 e depois para int64.
import numpy as np
a = np.array([1,2,3])

a = a.astype(np.float32)
a = a.astype(np.int64)
print(a, a.dtype)
