
months = 30
pairsPer = 5

childRabbits = 1
adultRabbits = 0

for i in range(1, months):
    temp = adultRabbits * pairsPer
    adultRabbits = adultRabbits + childRabbits
    childRabbits = temp
    
    
print("Immortal Rabbits\n------------")
print(childRabbits + adultRabbits)

print()

months = 89
maxAge = 17

childRabbits = 1
adultRabbits = 0

ageTracker = []
for i in range(0, maxAge):
    ageTracker.append(0)
ageTracker[len(ageTracker) - 1] = 1

#print(ageTracker)

for i in range(1, months):
    #print("Current Iteration: " + str(i) + " - Amt: " + str(childRabbits + adultRabbits) + " Child - Adult: " + str(childRabbits) + " " + str(adultRabbits))
    #print(ageTracker)

    temp = adultRabbits
    cAge = temp
    adultRabbits = adultRabbits + childRabbits
    mAge = 0
    rabbitsToRemove = 0
    for j in reversed(range(len(ageTracker))):
        mAge = ageTracker[j]
        ageTracker[j] = cAge
        cAge = mAge
        if j == 0:
            rabbitsToRemove = mAge
    adultRabbits -= rabbitsToRemove
    if adultRabbits < 0:
        adultRabbits = 0
    childRabbits = temp

    #print("Current Iteration: " + str(i) + " - Amt: " + str(childRabbits + adultRabbits) + " Child - Adult: " + str(childRabbits) + " " + str(adultRabbits))
    #print(ageTracker)
    #print("----")
    

print("Mortal Rabbits\n------------")
print(childRabbits + adultRabbits)