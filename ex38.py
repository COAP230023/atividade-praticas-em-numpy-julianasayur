# 38. PCA básica (autovetores) (difícil)
# Implemente PCA 2D→1D: centralize X (N×2), calcule covariância, autovetores, projete em 1D e
# reconstrua aproximado.
import numpy as np
rng = np.random.default_rng(0)
N = 100
X = rng.normal(size=(N, 2))
mean = X.mean(axis=0)
Xc = X - mean
C = np.cov(Xc, rowvar=False)

eigvals, eigvecs = np.linalg.eigh(C)
idx = eigvals.argsort()[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

v1 = eigvecs[:, 0] 

X_1D = Xc @ v1 
X_reconstructed = np.outer(X_1D, v1) + mean 

print("Média original:")
print(mean)
print("\nAutovalores (maior primeiro):")
print(eigvals)
print("\nPrimeiro autovetor (direção principal):")
print(v1)
print("\nPrimeiras 5 projeções (1D):")
print(X_1D[:5])
print("\nPrimeiras 5 reconstruções aproximadas:")
print(X_reconstructed[:5])