# 2a
v1 = []
for i in range(67):
    if i < 35:
        v1.append(4*i - 5)
    else:
        v1.append(9 - 3*i)

# or

v1_alt = [4*i - 5 if i < 35 else 9 - 3*i for i in range(67)]

print(v1)

# 2b
v2 = v1[22:44]
print(v2)

# 2c
v1.reverse()
v3 = v1[:65]
print(v3)


