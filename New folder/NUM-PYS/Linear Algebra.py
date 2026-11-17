import numpy as np
u_list=[1,2,3]
v_list=[4,5,6]
u=np.array([1,2,3])
v=np.array([4,5,6])
vector_sum=u+v
scaled_vector=2*u
dot_product_numpy=u@v  
print (f"NumPy Dot Product:{dot_product_numpy}")
X=np.array([
    [25,50000],
    [30,65000],
    [45,90000]
])
w=np.array([1.5,0.0002])
predictions=X@w
print(f"Model Predictions:{predictions}")