import numpy as np


# 6a
def pp(i, x, xs):
    return np.prod(list((x - xs[j])/(xs[i] - xs[j]) for j in range(len(xs)) if i != j))
    # np.prod is just capital Pi (product of elements in a list).


# 6b
xx = [0.1, 0.2, 0.3, 0.4]
yy = [10, 5, -3, -8]

# 6c
def inter(x):
    return sum(pp(i, x, xx) * yy[i] for i in range(len(yy)))

'''
A = np.array([[i**2 + 3**(i+j) for j in range(1,7)] for i in range(1,7)], float)
B = np.zeros((6,6))
for i in range(1 ,7):
    for j in range(1, 7):
        B[i -1, j-1] = i**2 + 3**(i + j)

print(np.linalg.det(A))
print(np.linalg.det(B))'''