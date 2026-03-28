# 17. Frequências inteiras (fácil)
# Gere 100 inteiros aleatórios em [0,9] e conte as frequências de cada valor (0 a 9).
import numpy as np
import numpy as np
v = np.random.randint(0, 10, size=100)
freq = np.bincount(v, minlength=10)
print("Vetor gerado:\n", v)
print("\nFrequências de 0 a 9:\n", freq)