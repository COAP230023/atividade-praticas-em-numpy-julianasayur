# 41. Regressão linear (OLS) com NumPy (difícil)
# Dado X (N×d) e y, calcule os coeficientes OLS usando np.linalg.lstsq e avalie RMSE no
# treino.
import numpy as np

X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5]
])

y = np.array([2, 3, 5, 7, 11])

coef, *_ = np.linalg.lstsq(X, y, rcond=None)

y_pred = X @ coef

rmse = np.sqrt(np.mean((y - y_pred) ** 2))

print("Coeficientes:", coef)
print("Predições:", y_pred)
print("RMSE:", rmse)