# 35. Covariância e correlação (médio)
# Simule uma matriz 1000×3 de N(0,1) e compute cov (colunas como variáveis) e corrcoef.
import numpy as np
X = np.random.randn(1000, 3) 

cov = np.cov(X, rowvar=False)

corr = np.corrcoef(X, rowvar=False)

print("Matriz X (1000x3):")
print(X[:5]) 
print("\nCovariância:")

print(cov)
print("\nCorrelação:")
print(corr)