
months = 30
pairsPer = 5

childRabbits = 1
adultRabbits = 0

for i in range(1, months):
    temp = adultRabbits * pairsPer
    adultRabbits = adultRabbits + childRabbits
    childRabbits = temp
    
    

print(childRabbits + adultRabbits)
