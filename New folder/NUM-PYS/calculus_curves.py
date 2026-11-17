import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,3.5,400)
y=x**3-3*x**2
dy_dx=3*x**2-6*x
plt.figure(figsize=(9,6))
plt.plot(x, y, label=r"$f(x)=x^3-3x^2+2$", color="blue",linewidth=2)
plt.plot(x,dy_dx,label=r"$f'(x)=3x^2-6x$",color="red",linestyle="--",linewidth=2)
x_fill=np.linspace(0, 2, 100)
y_fill=x_fill**3-3*x_fill**2+2
plt.fill_between(x_fill,y_fill,color="skyblue",alpha=0.4, label=r"integral Area$\int_{0}^{2} f(x)dx$")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Calculus:Functions, Derivatives & Integrals", fontsize=14, fontweight='bold')
plt.xlabel('x',fontsize=12)
plt.ylabel(Outputs:='y',fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--',alpha=0.6)
plt.show()
