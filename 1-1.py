file = open("1-1.in", "r")

total = 0
for line in file:
    fuel = int(line.strip()) // 3 - 2
    total += fuel

print(total)
