from io import StringIO
from pathlib import Path


seqMap = {}
gcMap = {}

f = open(str(Path(__file__).parent) + "\\gccontent.txt")

curLine = f.readline()

curSeqName = ""
curSeq = StringIO()
first = True

while curLine != "":
    print(curLine)

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

highestSeqName = ""
highestSeqGC = 0

for seqName in seqMap.keys():

    total = 0
    totalGC = 0
    
    for i in seqMap[seqName]:
        if i == "G" or i == "C":
            total += 1
            totalGC += 1
        else:
            total += 1
    
    gcPercent = (totalGC / total) * 100
    gcMap[seqName] = gcPercent

    if gcPercent > highestSeqGC:
        highestSeqName = seqName
        highestSeqGC = gcPercent



print(highestSeqName)
print(highestSeqGC)