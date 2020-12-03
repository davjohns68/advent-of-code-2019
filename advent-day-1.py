inputFile = open("day1-input.txt", "r")
moduleMasses=[]
for item in inputFile:
    moduleMasses.append(int(item))

# PART 1
totalFuel=0
for mass in moduleMasses:
    totalFuel += mass // 3 - 2

print(totalFuel)

# PART 2
totalFuel = 0
for mass in moduleMasses:
    while mass > 0:
        fuelForMass = mass // 3 - 2
        if fuelForMass <= 0:
            mass = 0
            continue
        totalFuel += fuelForMass
        mass = fuelForMass
print(totalFuel)