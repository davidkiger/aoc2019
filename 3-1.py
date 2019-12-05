file = open("3-1.in", "r")

wires = []
for line in file:
    wires.append(line.strip().split(','))


def make_grid(wire):
    grid = {}
    x = 0
    y = 0
    for inst in wire:
        d = inst[0]
        v = int(inst[1:])
        if d == 'U':
            inc = (0, 1)
        elif d == 'D':
            inc = (0, -1)
        elif d == 'L':
            inc = (-1, 0)
        elif d == 'R':
            inc = (1, 0)

        for i in range(v):
            x += inc[0]
            y += inc[1]
            grid[(x, y)] = 1

    return grid

grid1 = make_grid(wires[0])
grid2 = make_grid(wires[1])

pairs = set(grid1.keys()).intersection(set(grid2.keys()))
dists = [abs(x)+abs(y) for (x, y) in pairs]

print(min(dists))
