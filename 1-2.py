file = open("1-1.in", "r")

total = 0
for line in file:
    fuel = int(line.strip()) // 3 - 2
    while fuel > 0:
        total += fuel
        fuel = fuel // 3 - 2

print(total)
