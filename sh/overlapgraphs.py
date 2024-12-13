from io import StringIO
from pathlib import Path

k = 3

seqMap = {}

f = open(str(Path(__file__).parent) + "\\overlapgraphs.txt")

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
            seqMap[curSeqName] = curSeq.getvalue().replace("\n", "")
            curSeqName = ""
            curSeq = StringIO()

        curSeqName = curLine[1 : len(curLine) - 1]

    else:
        curSeq.write(curLine)

    curLine = f.readline()

if curSeqName != "":
    seqMap[curSeqName] = curSeq.getvalue().replace("\n", "")
    curSeqName = ""
    curSeq = StringIO()

graph = {}

for seq in seqMap.keys():
    graph[seq] = []

for seq in graph.keys():
    for seqN in seqMap.keys():
        if seq == seqN:
            continue
        if seqMap[seq] == seqMap[seqN]:
            continue

        seqK = seqMap[seq][len(seqMap[seq]) - k : len(seqMap[seq])]
        seqNK = seqMap[seqN][0 : k]

        if seqK == seqNK:
            graph[seq].append(seqN)

print(graph)

c = 0

for seq in graph.keys():
    for seqN in graph[seq]:
        c += 1
        print(seq + " " + seqN)

print(c)
#print(seqMap)