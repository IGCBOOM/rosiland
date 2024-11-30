import math
import itertools

n = 7

p = math.factorial(n)

lst = []
for i in range(n):
    lst.append(i + 1)

fPerms = list(itertools.permutations(lst))
with open('out.txt', 'w') as output:
    output.write(str(p))
    output.write('\n')
    #print(fPerms)
    for perm in fPerms:
        for i in range(n):
            output.write(str(perm[i]) + " ")
        output.write('\n')