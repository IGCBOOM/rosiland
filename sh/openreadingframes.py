from io import StringIO

dnaSeq = "ACCAAGTCAACGCGGCCCCCCTGACCTGCCAACGACTCGATCAGGGTTTAGTCTAGGCCTTCCTTGTACTAAGGGCGTACAGCGGGGCCTAATCAGCCTCAAGCGCACTCCCAAATCTATATGGTAAGTAACCAGGGTCGTCGATGGGAGGCATGGTGGTTCACCTCGGGTCATAAGCCGTCGGCACACCCACACAACGCGCACATGCTACTGACCCGGCAGCGACTGAGACCAGCTACACGTGTGTCCACAGGGGTGTAATCCATCAAACGGCAGCCAGCTCTTTTATCATTTCCTCCCATGGCTAGGAGGGTGCGATTCAATGTTGCTTCCGAGACGTGTTTTATCAAAGCAACCAACCCCCGTGTATCCGAAATAAAATAAGAGCACACTCACCCGGGGCCGATCTGCACCCGGGATCACTAACCTGTTGCAGCGGTTATCCGGACTCATGAATCCGAGCGGTATCTCAAAGGCTTACTAGCTAGTAAGCCTTTGAGATACCGCTCGGATTCATTCCACACCCAAGCTATGCTTGAACTTTACGGCGCTTCCCAAGCCTGAGCGCACGGTACATCGAAAGGAGCTGGCTTGCGGTAACCATGTAACAGTCCTTTTTCTAGGGTTTCTGCTCCGCTGACAGCACGTTTCGGTGGCTTACCAAGGATGCTCCGTTGCATCAACCCTTTGGGAGAAATGTCAGGAATATACGCCGAGATGATACGCAAACCGGAAATGGCATGGCAGGCCCACGATTGATGTCGTTATATATCAGACGGCGGTCTCCTTGTTCTGAATCGAGGTTTGGTTTTTTCCTCCACCCGTACCTGTACGAAATCACAGAATAGGTTCGAAACGTGCGTAGGCACGCGACACTTGGGTGTAATAACCCTGCAAGTCCGCAGGTTGCGCTGACCTTATCAACATTGACGCCCCATCGCACCACTCTGCACGCCCGAGTCTGCTTA"
reverseComp = ""

cStr = StringIO()

for n in reversed(dnaSeq):
    match n:
        case 'A':
            cStr.write('T')
        case 'T':
            cStr.write('A')
        case 'G':
            cStr.write('C')
        case 'C':
            cStr.write('G')

reverseComp = cStr.getvalue()

dnaStrings = [ dnaSeq, reverseComp ]

rnaSeqs = []

for dnaStr in dnaStrings:
    rnaSeqs.append(dnaStr.replace("T", "U"))

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

proteinSeqList = {"", ""}

for rnaSeq in rnaSeqs:
    for i in range(len(rnaSeq)):
        if rnaSeq[i : i + 3] == "AUG":
            curCodon = rnaSeq[i : i + 3]
            idx = i
            nostop = False
            while seqMap[curCodon] != "---":
                proteinSeq.write(seqMap[curCodon])
                idx += 3
                curCodon = rnaSeq[idx : idx + 3]
                if curCodon == "":
                    #print("Empty String ?!?!")
                    nostop = True
                    break
            if nostop:
                continue
            proteinSeqList.add(proteinSeq.getvalue())
            proteinSeq = StringIO()

#print(proteinSeqList)

for seq in proteinSeqList:
    if seq != "":
        print(seq)