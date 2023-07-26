def lerFASTA(seq):
    with open(seq, 'r') as f:
        return [line.strip() for line in f.readlines()]


seqlist = lerFASTA('MatrixConsensusData.py')
seqDict = {}
seqLabel = ''
for i, v in enumerate(seqlist):
    if i % 2 == 0:
        seqLabel = v
        seqDict[seqLabel] = ''
    else:
        seqDict[seqLabel] = v
seqListfinal = []
matrixLine = []
matrixfinal = []
matrixDict = {"A": 0, "C": 0, "G": 0, "T": 0}
seqconsensus = ''
profileMatrix = {"A": [], "C": [], "G": [], "T": []}

for k, v in seqDict.items():
    seqListfinal.append(v)
contline = 0

for v in range(len(seqListfinal) + 1):
    for i, value in enumerate(seqListfinal):
        if v == contline + 1 and (v < len(seqListfinal[0])):
            matrixfinal.append(matrixLine[:])
            matrixLine.clear()
            matrixLine.append(seqListfinal[i][v])
            contline += 1
        elif v < len(seqListfinal[0]):
            matrixLine.append(seqListfinal[i][v])
matrixfinal.append(matrixLine[:])


# # matrix final dos dados:
# print(matrixfinal)
#
# for v in range(0,len(matrixfinal[0])+1):
#     for i, value in enumerate(matrixfinal):
#         if v < (len(matrixfinal[0])):
#             print(matrixfinal[i][v],end='')
#     print()


cont = 0
for i, value in enumerate(matrixfinal):
    if i > cont:
        # encerrar a leitura da chave e add nuc à seq consenso
        seqconsensus += max(matrixDict, key=matrixDict.get)
        profileMatrix["A"].append(matrixDict["A"])
        profileMatrix["C"].append(matrixDict["C"])
        profileMatrix["G"].append(matrixDict["G"])
        profileMatrix["T"].append(matrixDict["T"])
        # limpar dicionario
        matrixDict = {"A": 0, "C": 0, "G": 0, "T": 0}
        cont = i
    for v in value:
        matrixDict[v] += 1
profileMatrix["A"].append(matrixDict["A"])
profileMatrix["C"].append(matrixDict["C"])
profileMatrix["G"].append(matrixDict["G"])
profileMatrix["T"].append(matrixDict["T"])

seqconsensus += max(matrixDict, key=matrixDict.get)
print(seqconsensus)


for k, v in profileMatrix.items():
    print(f'{k}: ', end='')
    for values in v:
        print(values,end=' ')
    print()


# FASTAGC = {}
# FASTAGC = {k: gc_content(v) for k,v in FASTAdict.items()}
# MaxGCKey = max(FASTAGC, key=FASTAGC.get)
# print(f'{MaxGCKey[1:]}\n{FASTAGC[MaxGCKey]}')


# print(len(seqDict.keys()))
# print(len(seqDict))
# print(seqDict.values())
# print(seqDict)
# cont = 0
# for k, v in seqDict.items():
#     for i, val in enumerate(seqDict.values()):
#         print(val[cont])
#     cont +=1
