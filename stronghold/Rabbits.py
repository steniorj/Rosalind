def recurrence_relation(n,k):
    t_menos_1 = 1
    t_menos_2 = 0
    t = 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        for itr in range(n-1):
            t = (t_menos_2*k) + t_menos_1
            t_menos_2 = t_menos_1
            t_menos_1 = t
    return t

print(recurrence_relation(32,5))