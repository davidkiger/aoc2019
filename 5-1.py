file = open("5-1.in", "r")

for line in file:
    prog = list(map(int, line.strip().split(',')))


def get_params(prog, vals, modes):
    while len(modes) < len(vals):
        modes.append(0)
    modes[len(modes)-1] = 1
    return [x if modes[i] == 1 else prog[x] for i, x in enumerate(vals)]

INPUT = 1
ip = 0

while True:
    digits = list(map(int, str(prog[ip])))
    opcode = digits[-1]
    if len(digits) > 1:
        opcode += digits[-2]*10
    modes = digits[:-2]
    modes = modes[::-1]

    if opcode == 1:
        params = get_params(prog, prog[ip+1:ip+4], modes)
        prog[params[2]] = params[0] + params[1]

    elif opcode == 2:
        params = get_params(prog, prog[ip+1:ip+4], modes)
        prog[params[2]] = params[0] * params[1]

    elif opcode == 3:
        params = [prog[ip+1]]
        prog[params[0]] = INPUT

    elif opcode == 4:
        params = [prog[ip+1]]
        print(prog[params[0]])

    elif opcode == 99:
        print('done')
        exit()

    ip += len(params) + 1
