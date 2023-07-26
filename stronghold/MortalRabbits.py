def mortal_rabbits(num,m):
    adulto_n_menos_2 = 0
    adultn_1 = 1
    adultn = 1
    filhotesn = 1
    filhotesn_1 = 0
    filhotes_dict = {0: 0, 1: 1, 2: 0}
    totaln = 2
    dictLabel = m
    if num == 1:
        return 1
    if num == 2:
        return 1
    for itr in range(num - 2):
        dictLabel = m
        adultn = adultn_1 + filhotesn_1 - filhotes_dict[itr]
        print(adultn,adultn_1,filhotesn_1,filhotes_dict)
        filhotesn = adultn_1
        print(filhotesn,'filhotesn')
        filhotes_dict[itr+3] = filhotesn
        totaln = adultn + filhotesn
        print(totaln,'totaln')
        adulto_n_menos_2 = adultn_1
        adultn_1 = adultn
        filhotesn_1 = filhotesn
        print()



    return totaln

print(mortal_rabbits(7),'disc')