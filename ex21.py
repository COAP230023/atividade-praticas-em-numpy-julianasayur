# 21. Datas básicas (fácil)
# Crie um array de datas diárias de 2025-01-01 a 2025-01-07 (inclusive).
import numpy as np
datas = np.arange("2025-01-01", "2025-01-08", dtype="datetime64[D]")
print(datas)