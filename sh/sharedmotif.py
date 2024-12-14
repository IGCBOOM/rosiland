
from io import StringIO
from pathlib import Path

foundZero = False

sequences = []

f = open(str(Path(__file__).parent) + "\\sharedmotif.txt")

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

minSeq = ""
minSeqLen = 1000000000
for seq in sequences:
    if len(seq) < minSeqLen:
        minSeq = seq
        minSeqLen = len(seq)  

k = 215

while foundZero != True:
    kmers = set()

    # get unique k-mers in data string
    for i in range(len(minSeq)):
        if i == len(minSeq) - k:
            break
        kmers.add(minSeq[i:i+k])

    lastKmerFound = ""
    lastKmerCount = 0

    for kmer in kmers:
    
        for seq in sequences:

            foundInSeq = False

            for i in range(len(seq)):
                if seq[i:i+k] == kmer:
                    foundInSeq = True

            if foundInSeq == True:
                lastKmerCount += 1

        if lastKmerCount == len(sequences):
            lastKmerFound = kmer
        lastKmerCount = 0

    print("Last common kmer found for k = " + str(k) + " = " + lastKmerFound)

    if lastKmerFound == "":
        foundZero = True
        print("Found Zero!")

    k += 1
