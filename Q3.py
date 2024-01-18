import numpy as np

# 3a
v1 = [4*i - 5 if i < 35 else 9 - 3*i for i in range(67)]

w = np.array(v1)
w = np.atleast_2d(w)  # Allows us to calculate the transpose. Returns a 1 x 67 vector.

# 3b
identity = np.identity(67)  # 67 x 67 identity matrix.
wT = w.transpose()  # A 67 x 1 vector.
# Ok so there are two ways of doing this depending on the dimension of w. If w is (1x67), then we'll get a scalar
# when we multiply it by its transpose. However, if w is (67x1), we'll get a (67x67) matrix.

A1 = identity + np.matmul(wT, w)  # np.matmul(wT, w) is a 67 x 67 matrix.
A2 = identity + np.matmul(w, wT)  # np.matmul(w, wT) is a scalar.
# Both A1 and A2 are 67 x 67 matrices.

# 3c
# Ok so this only works when w is a (67x1) vector, so I'm gonna guess you use A1 but I'll double-check.
print(np.linalg.solve(A1, wT))
