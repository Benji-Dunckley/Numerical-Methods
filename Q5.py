# 5A
y = (lambda x: 4*x*(1-x))
# or
def y_alt(x):
    return 4*x*(1-x)

# 5B
def lo_gen(n):  # n = length of list - 1
    lo = [0.3]
    for i in range(1, n+1):
        lo.append(y(lo[i-1]))
    return lo

# 5C
def ma(n):
    lo = lo_gen(n+1)
    nl = []
    for i in range(n+1):
        nl.append(lo[i] - lo[i+1])
    print(f'List:\n{nl}\nMax Element:\n{max(nl)}\nIndex of Max:\n{nl.index(max(nl))}')
    # max(list) returns max element and list.index(list element returns the index of that element)







