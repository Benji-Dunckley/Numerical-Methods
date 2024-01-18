import numpy as np


# 7a
def verlet(y0, y1, h, n, f):
    ys = [y0, y1]
    for i in range(n-2):
        ys.append(2*ys[-1] - ys[-2] + f(ys[-1]) * h ** 2)

    return np.array(ys)


# 7b
y_sol = verlet(0, 0.1, 0.1, 100, lambda x: -x)
print(y_sol)

# 7c
print(f'Difference is equal to {abs(y_sol[48] - np.sin(4.8))}')