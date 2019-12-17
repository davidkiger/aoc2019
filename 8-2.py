file = open("8-1.in", "r")

w = 25
t = 6

arr = []
for line in file:
    arr = map(int, list(line.strip()))

layers = []
while len(arr) >= w*t:
    layers.append(arr[:w*t])
    arr = arr[w*t:]


top = layers[0][:]
for i in range(1, len(layers)):
    for p in range(0, len(layers[i])):
        if top[p] == 2:
            top[p] = layers[i][p]

for i in range(0, t):
    row = ''
    for j in range(0, w):
        idx = i*w+j
        if top[idx] == 1:
            top[idx] = '#'
        if top[idx] == 0:
            top[idx] = ' '
        row += str(top[idx])
    print(row)
