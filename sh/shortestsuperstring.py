from io import StringIO
from pathlib import Path

seqMap = {}

f = open(str(Path(__file__).parent) + "\\shortestsuperstring.txt")

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

# find overlaps of each dna string between each other. (75% -> 50%)

beginOverlaps = {}
endOverlaps = {}

# find best beginning overlap for each string (beginning of one string to end of another)

for name in seqMap:
    beginOverlaps[name] = ("", -1)

    for name2 in seqMap:

        if name == name2:
            continue

        dnaSeq = seqMap[name]
        dnaSeq2 = seqMap[name2]
        dnaSeqLen = len(dnaSeq)
        dnaSeq2Len = len(dnaSeq2)
        
        sP = int(dnaSeqLen * 0.75)
        fP = int(dnaSeqLen * 0.5)
        
        curPos = sP
        highestMatch = -1
        highestMatchName = ""

        while curPos != fP:

            if highestMatch != -1:
                break

            dontMatch = False

            j = 0

            for i in range(dnaSeqLen - curPos, dnaSeqLen):

                if dnaSeq[i] != dnaSeq2[j]:
                    dontMatch = True
                    #print("kill " + name + " " + name2)
                    break

                j += 1

            if not dontMatch:
                if highestMatch < curPos:
                    #print("good " + name + " " + name2)
                    highestMatch = curPos
                    highestMatchName = name2

            curPos -= 1

        if highestMatch != -1:
            if beginOverlaps[name][1] <= highestMatch:
                beginOverlaps[name] = (highestMatchName, highestMatch)

        
# construct sequence via overlap scoring

orderedSeqs = []

curRevSeq = "FIRSTSEQ"
foundEnd = False

while not foundEnd:
    foundT = False
    for overlapSeq in beginOverlaps.keys():
        if curRevSeq == "FIRSTSEQ":
            #print("test: " + str(beginOverlaps[overlapSeq]) + " " + str(beginOverlaps[overlapSeq][1]))
            if beginOverlaps[overlapSeq][1] == -1:
                curRevSeq = overlapSeq
                orderedSeqs.append((overlapSeq, beginOverlaps[overlapSeq]))
                #print("found end")
                foundT = True
                break
        else:
            if beginOverlaps[overlapSeq][0] == curRevSeq:
                curRevSeq = overlapSeq
                orderedSeqs.append((overlapSeq, beginOverlaps[overlapSeq]))
                foundT = True
                break
    
    if not foundT:
        #print("end")
        foundEnd == True
        break


orderedSeqs = orderedSeqs[::-1]

#print(curRevSeq)
#print(orderedSeqs)

curSeq = ""
firstComb = True

#print(curSeq[0 : len(curSeq) - 7])

for seqPair in orderedSeqs:
    if seqPair[1][1] == -1:
        break

    if firstComb:
        curSeq = seqMap[seqPair[0]][0 : len(seqMap[seqPair[0]]) - seqPair[1][1]] + seqMap[seqPair[1][0]]
        #print("Cool: " + seqMap[seqPair[0]][0 : len(seqMap[seqPair[0]]) - seqPair[1][1]])
        firstComb = False
    else:
        curSeq = curSeq[0 : len(curSeq) - seqPair[1][1]] + seqMap[seqPair[1][0]]
print(curSeq)

    
    



#print(beginOverlaps)