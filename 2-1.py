file = open("2-1.in", "r")

for line in file:
    prog = list(map(int, line.strip().split(',')))
    prog[1] = 12
    prog[2] = 2

ip = 0
while(prog[ip] != 99):
    params = (prog[ip+1], prog[ip+2], prog[ip+3])
    if prog[ip] == 1:
        prog[params[2]] = prog[params[0]] + prog[params[1]]
    elif prog[ip] == 2:
        prog[params[2]] = prog[params[0]] * prog[params[1]]
    ip += len(params) + 1

print(prog[0])
