# 42. Rolling window 2D com strides (difícil)
# Usando sliding_window_view, compute a média local 3×3 de uma imagem 2D sem laços
# explícitos.
import numpy as np

img = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
], dtype=float)

janelas = np.lib.stride_tricks.sliding_window_view(img, (3, 3))

media_local = janelas.mean(axis=(2, 3))

print("Imagem original:\n", img)
print("\nMédias locais 3×3:\n", media_local)