def mortal_rabbits(month,m=3):
    # iniciando variaveis para month = 1
    adultosN = 0
    filhotesN = 1
    adultosN_1 = 0
    filhotesN_1 = 0
    totalrabbitsN = (adultosN + filhotesN)
    
    #preparando o dicionario com filhotes nascidos no mes atual
    filhotesDict ={}
    for v in range(-20,1):
        filhotesDict[v] = 0
    filhotesDict[1] = 1
    print(filhotesDict)
    #

    if month == 1:
        return 1

    #var inicia com 0
    for var in range(month-1):
        print('var:',var)
        #setar variaveis para month atual:
        
        #variavel para calcular NFn-3
        filhotesIndex = (var+2)-m
        
        #trasferindo N para N-1
        adultosN_1 = adultosN
        filhotesN_1 = filhotesN
        print(adultosN_1,'adultosN_1')
        print(filhotesN_1,'filhotesN_1')

        #calculando novo N
        adultosN = (adultosN_1 + filhotesN_1) - filhotesDict[filhotesIndex]
        filhotesN = adultosN_1
        print(adultosN,'adultosN')
        print(filhotesN,'filhotesN')
        totalrabbitsN = adultosN + filhotesN
        print(totalrabbitsN,'totalrabbitsN')

        #atualizar dicionario com filhotes nascidos nesse mes
        filhotesDict[var+2] = adultosN_1
        print(filhotesDict)

    return totalrabbitsN

print(mortal_rabbits(90,m=16),'print return var')