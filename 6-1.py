from collections import defaultdict

file = open("6-1.in", "r")

orbits = defaultdict(list)
for line in file:
    (a, b) = line.strip().split(')')
    orbits[a].append(b)


def orbit_count(obj, count, total):
    total += count
    for b in orbits[obj]:
        total = orbit_count(b, count+1, total)
    return total

print(orbit_count('COM', 0, 0))
