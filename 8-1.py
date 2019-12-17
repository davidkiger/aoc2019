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

min_arr = None
min_zeroes = 10000
for l in layers:
    zeroes = l.count(0)
    if zeroes < min_zeroes:
        min_arr = l
        min_zeroes = zeroes

print(min_arr.count(1) * min_arr.count(2))
