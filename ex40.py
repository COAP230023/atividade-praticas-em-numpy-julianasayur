# 40. Sistemas lineares e resíduo (difícil)
# Gere uma matriz A (100×100) bem-condicionada, um vetor b e resolva Ax=b com
# np.linalg.solve. Compute o resíduo relativo ||Ax−b||/||b|| e cond(A).
import numpy as np

rng = np.random.default_rng(0)

n = 100

M = rng.normal(size=(n, n))
Q, _ = np.linalg.qr(M) 

eigs = np.linspace(1.0, 10.0, n)
D = np.diag(eigs)

A = Q @ D @ Q.T

x_true = rng.normal(size=n)
b = A @ x_true

x = np.linalg.solve(A, b)

residual_rel = np.linalg.norm(A @ x - b) / np.linalg.norm(b)

cond_A = np.linalg.cond(A)

print(f"cond(A) ≈ {cond_A:.6g}")
print(f"Resíduo relativo ||Ax - b||/||b|| = {residual_rel:.3e}")
print(f"Erro relativo na solução ||x - x_true||/||x_true|| = {np.linalg.norm(x - x_true)/np.linalg.norm(x_true):.3e}")
