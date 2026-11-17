import numpy as np
A=np.array ([
    [1,-3,3],
    [3,-5,3],
    [6,-6,4]
])
eigenvalues, eigenvectors= np.linalg.eig(A)
print("Eigenvalues(Variancemagnitude):\n",eigenvalues)
print("\nEigenvectors(Principal axes):\n", eigenvectors)