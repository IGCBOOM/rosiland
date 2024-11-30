import itertools

n = 3

lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

fPerms = [p for p in itertools.product(lst, repeat=n)]
with open('out.txt', 'w') as output:
    for perm in fPerms:
        for i in range(n):
            output.write(str(perm[i]))
        output.write('\n')