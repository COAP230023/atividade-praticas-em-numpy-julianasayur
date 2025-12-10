# 28. Precisão de média (médio)
# Gere 1_000_000 floats uniformes em [0,1) e compute a média. Compare com o valor teórico
# 0.5 (erro absoluto).
import numpy as np
x = rng.random(1_000_000)
erro = abs(x.mean() - 0.5)
print("Erro:", erro)