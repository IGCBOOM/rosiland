from io import StringIO
from pathlib import Path

fSeq = True

sequence = ""
introns = []

f = open(str(Path(__file__).parent) + "\\rnasplicing.txt")

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
            if fSeq:

                sequence = curSeq.getvalue().replace("\n", "")
                curSeqName = ""
                curSeq = StringIO()
                fSeq = False

            else:

                introns.append(curSeq.getvalue().replace("\n", ""))
                curSeqName = ""
                curSeq = StringIO()

        curSeqName = curLine[1 : len(curLine) - 1]

    else:
        curSeq.write(curLine)

    curLine = f.readline()

if curSeqName != "":
    introns.append(curSeq.getvalue().replace("\n", ""))
    curSeqName = ""
    curSeq = StringIO()

for intron in introns:
    sequence = sequence.replace(intron, "")

rnaSeq = sequence.replace("T", "U")

#print(rnaSeqs)

proteinSeq = StringIO()

seqMap = { "UUU": 'F', "UUC": 'F', "UUA": 'L', "UUG": 'L', "UCU": 'S', "UCA": 'S', "UCC": 'S', "UCG": 'S', 
          "UAU": 'Y', "UAC": 'Y', "UAA": '---', "UAG": '---', "UGU": 'C', "UGC": 'C', "UGA": '---', "UGG": 'W', 
          "CUU": 'L', "CUC": 'L', "CUA": 'L', "CUG": 'L', "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P', 
          "CAU": 'H', "CAC": 'H', "CAA": 'Q', "CAG": 'Q', "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R', 
          "AUU": 'I', "AUC": 'I', "AUA": 'I', "AUG": 'M', "ACU": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T', 
          "AAU": 'N', "AAC": 'N', "AAA": 'K', "AAG": 'K', "AGU": 'S', "AGC": 'S', "AGA": 'R', "AGG": 'R', 
          "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V', "GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A', 
          "GAU": 'D', "GAC": 'D', "GAA": 'E', "GAG": 'E', "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G', }

proteinSequence = ""
#print(rnaSeq)

done = False

for i in range(len(rnaSeq)):
    if rnaSeq[i : i + 3] == "AUG":
        curCodon = rnaSeq[i : i + 3]
        idx = i
        nostop = False
        while seqMap[curCodon] != "---":
            proteinSeq.write(seqMap[curCodon])
            idx += 3
            curCodon = rnaSeq[idx : idx + 3]
            if curCodon == "---":
                done = True
                break
        proteinSequence = proteinSeq.getvalue()
        proteinSeq = StringIO()
        break

print(proteinSequence)