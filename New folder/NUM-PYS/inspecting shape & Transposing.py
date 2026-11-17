import numpy as np
X=np.array([
    [25, 50000],
    [30, 65000],
    [45, 90000]
])
print(f"Shape of X:{X.shape}")
X_transposed =X.T
print(f"Shape of Transposed X:{X_transposed.shape}")
print("Transposed Matrix:\n", X_transposed)
