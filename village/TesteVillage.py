outputFile = []

with open("input.txt",'r') as f:
    outputFile = [line.strip() for line in f.readlines()]

print(outputFile)