
k = 17 # Homozygous dominant
m = 23 # Heterozygous
n = 16 # Homozygous recessive

total = k + m + n
totalM = total - 1

finalProb = 0
finalProb += (k / total)
finalProb += ((m / total) * (k / totalM))
finalProb += (((m / total) * ((m - 1) / totalM)) * .75)
finalProb += (((m / total) * (n / totalM)) * .5)
finalProb += ((n / total) * (k / totalM))
finalProb += ((n / total) * (m / totalM) * .5)
#finalProb += (((m / total) * ((n - 1) / totalM)) * 0)

print(finalProb)