def fibonacci(n):
    t1 = 0
    t2 = 1
    if n == 0:
        return 0
    else:
        for itr in range(n - 1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3

    return t3

print(fibonacci(22))