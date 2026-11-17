import numpy as np
import matplotlib.pyplot as plt
A=np.array([[0,-2],
            [2,0]])
x=np.linspace(-5,5,20)
y=np.linspace(-5,5,20)
X,Y=np.meshgrid(x,y)
U=A[0,0]*X+A[0,1]*Y
V=A[1,0]*X+A[1,1]*Y
M=np.hypot(U,V)
plt.figure(figsize=(8,8))
plt.streamplot(X,Y,U,V,color=M, linewidth=1.5,cmap='viridis',density=1.5)
plt.plot(0,0,'ro',markersize=8,label='Equlibrium Point')
plt.title('Phase Potrait: Saddle Point', fontsize=16,fontweight='bold')
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.grid(True,linestyle='--',alpha=0.6)
plt.legend()
plt.show()