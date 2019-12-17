from collections import defaultdict

file = open("6-1.in", "r")

endpoints = []
visited = set()
orbits = defaultdict(list)
for line in file:
    (a, b) = line.strip().split(')')
    orbits[a].append(b)
    orbits[b].append(a)
    if b == 'YOU' or b == 'SAN':
        endpoints.append(a)


def transfer(obj, count):
    visited.add(obj)
    if obj == endpoints[1]:
        print(count)
        exit()

    for o in orbits[obj]:
        if o not in visited:
            transfer(o, count+1)

transfer(endpoints[0], 0)
