from io import StringIO
from pathlib import Path

sequences = []

f = open(str(Path(__file__).parent) + "\\consensus.txt")

curLine = f.readline()

curSeqName = ""
curSeq = StringIO()
first = True

while curLine != "":
    #print(curLine)

    if curLine[0] == ">":

        if first:
            first = False
        else:
            sequences.append(curSeq.getvalue().replace("\n", ""))
            curSeqName = ""
            curSeq = StringIO()

        curSeqName = curLine[1 : len(curLine) - 1]

    else:
        curSeq.write(curLine)

    curLine = f.readline()

if curSeqName != "":
    sequences.append(curSeq.getvalue().replace("\n", ""))
    curSeqName = ""
    curSeq = StringIO()

#print(sequences)

conSeq = StringIO()
A_c = []
C_c = []
G_c = []
T_c = []

for i in range(len(sequences[0])):

    totalA = 0
    totalC = 0
    totalG = 0
    totalT = 0

    for seq in sequences:
        match seq[i]:
            case 'A':
                totalA += 1
            case 'C':
                totalC += 1
            case 'G':
                totalG += 1
            case 'T':
                totalT += 1
    
    A_c.append(totalA)
    C_c.append(totalC)
    G_c.append(totalG)
    T_c.append(totalT)


for i in range(len(sequences[0])):
    maxN = max(A_c[i], C_c[i], G_c[i], T_c[i])
    if maxN == A_c[i]:
        conSeq.write('A')
        continue
    if maxN == C_c[i]:
        conSeq.write('C')
        continue
    if maxN == G_c[i]:
        conSeq.write('G')
        continue
    if maxN == T_c[i]:
        conSeq.write('T')
        continue

print(conSeq.getvalue())

print("A: ", end="")
for conNum in A_c:
    print(conNum, end=" ")
print(" ")
print("C: ", end="")
for conNum in C_c:
    print(conNum, end=" ")
print(" ")
print("G: ", end="")
for conNum in G_c:
    print(conNum, end=" ")
print(" ")
print("T: ", end="")
for conNum in T_c:
    print(conNum, end=" ")