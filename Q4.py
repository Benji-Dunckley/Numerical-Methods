import numpy as np
import matplotlib.pyplot as plt

# 4A
def g(x):
    return np.cos(np.pi * np.exp(x))

def h(x):
    return np.sin(np.pi * np.exp(x))


# 4B
xgrid = np.linspace(-5, 2, 200)
plt.plot(xgrid, g(xgrid))
plt.plot(xgrid, h(xgrid) + g(xgrid))
plt.show()

