# 37. k-means 2D (NumPy puro) (difícil)
# Implemente k-means com K=3 em pontos 2D: inicialize centróides aleatórios, faça 10 iterações
# de (1) atribuir pontos ao centróide mais próximo e (2) recomputar centróides.
import numpy as np

rng = np.random.default_rng(0)

N = 50
P = rng.normal(size=(N, 2))

K = 3 
it = 10 

idx = rng.choice(N, size=K, replace=False)
centroids = P[idx] 

for _ in range(it):

    dists = np.linalg.norm(P[:, None, :] - centroids[None, :, :], axis=2)
    labels = dists.argmin(axis=1) 

    new_centroids = np.zeros_like(centroids)
    for k in range(K):
        pts = P[labels == k]
        if len(pts) > 0:
            new_centroids[k] = pts.mean(axis=0)
        else:
            new_centroids[k] = P[rng.integers(0, N)]

    centroids = new_centroids

print("Centróides finais:")
print(centroids)
print("\nRótulos:")
print(labels)