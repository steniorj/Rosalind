def mendel_first_law(k=2, m=2, n=2):
    # k = homozigoto dominante/ m, heterozigoto / n = homozigoto recessivo
    eamostral = k+m+n
    #primeiro lance
    pK1 = k/eamostral
    pM1 = m/eamostral
    pN1 = n/eamostral
    #segundo lance apos K
    pKaposK = (k-1)/(eamostral-1)
    pMaposK = m / (eamostral-1)
    pNaposK = n / (eamostral-1)
    #segundo lance apos M
    pMaposM = (m-1) / (eamostral-1)
    pKaposM = (k) / (eamostral-1)
    pNaposM = (n) / (eamostral-1)
    #segundo lanco apos N
    pNaposN = (n-1) / (eamostral-1)
    pKaposN = (k) / (eamostral-1)
    pMaposN = (m) / (eamostral-1)
    #Probabilidade do evento dado K
    pKdadoK = pK1 * pKaposK
    pMdadoK = pK1 * pMaposK
    pNdadoK = pK1 * pNaposK
    #Probabilidade do evento dado M
    pMdadoM = pM1 * pMaposM
    pKdadoM = pM1 * pKaposM
    pNdadoM = pM1 * pNaposM
    #Probabilidade do evento dado N
    pNdadoN = pN1 * pNaposN
    pKdadoN = pN1 * pKaposN
    pMdadoN = pN1 * pMaposN
    #Probabilidades de haver pelo menos 1 alelo dominante
    pKK = 1
    pKM = 1
    pKN = 1
    pMM = 0.75
    pMN = 0.5
    pNN = 0
    #probabilidade dos eventos vezes a porcengatem de ao menos um alelo dominante
    pKdadoKeDominante = pKdadoK * pKK
    pMdadoKeDominante = pMdadoK * pKM
    pNdadoKeDominente = pNdadoK * pKN
    ## Com M no primeiro sorteio
    pMdadoMeDominante = pMdadoM * pMM
    pKdadoMeDominante = pKdadoM * pKM
    pNdadoMeDominante = pNdadoM * pMN
    ## Com N no primeiro sorteio
    pNdadoNeDominante = pNdadoN * pNN
    pKdadoNeDominante = pKdadoN * pKN
    pMdadoNeDominante = pMdadoN * pMN
    #Probabilidade final
    pfinal = pKdadoKeDominante + pMdadoKeDominante + pNdadoKeDominente\
             + pMdadoMeDominante +pKdadoMeDominante + pNdadoMeDominante\
            + pNdadoNeDominante + pKdadoNeDominante + pMdadoNeDominante
    
    return pfinal




print(mendel_first_law(16,27,21))