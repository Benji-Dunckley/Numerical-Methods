import numpy as np

# 1a
a = np.exp(np.cos(5) + 3)*np.log(np.pi)  # np.log is just the natural logarithm.

# 1b
# List comprehension:
def y(x):
    return sum(1 / (1 + x * j**2) for j in range(3, 201))

# For loop:
def y_alt(x):
    b = 0
    for i in range(3, 201):
        b += 1 / (1 + x * i**2)
    return b
