def puh(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(puh(float(input("First digit - ")), int(input("Second digit - "))))
