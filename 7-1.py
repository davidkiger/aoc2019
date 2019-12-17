from itertools import permutations

file = open("7-1.in", "r")

for line in file:
    original = list(map(int, line.strip().split(',')))


def get_params(opcode, prog, vals, modes):
    while len(modes) < len(vals):
        modes.append(0)
    if opcode != 5 and opcode != 6:
        modes[len(modes)-1] = 1
    return [x if modes[i] == 1 else prog[x] for i, x in enumerate(vals)]


def run_program(prog, inputs):
    ip = 0
    input_counter = 0
    opcode = -1
    OUTPUT = 0

    while opcode != 99:
        digits = list(map(int, str(prog[ip])))
        opcode = digits[-1]
        if len(digits) > 1:
            opcode += digits[-2]*10
        modes = digits[:-2]
        modes = modes[::-1]
        ipset = False

        if opcode == 1:
            params = get_params(opcode, prog, prog[ip+1:ip+4], modes)
            prog[params[2]] = params[0] + params[1]

        elif opcode == 2:
            params = get_params(opcode, prog, prog[ip+1:ip+4], modes)
            prog[params[2]] = params[0] * params[1]

        elif opcode == 3:
            params = [prog[ip+1]]
            prog[params[0]] = inputs[input_counter]
            input_counter += 1

        elif opcode == 4:
            params = [prog[ip+1]]
            OUTPUT = prog[params[0]]

        elif opcode == 5:
            params = get_params(opcode, prog, prog[ip+1:ip+3], modes)
            if params[0] != 0:
                ip = params[1]
                ipset = True

        elif opcode == 6:
            params = get_params(opcode, prog, prog[ip+1:ip+3], modes)
            if params[0] == 0:
                ip = params[1]
                ipset = True

        elif opcode == 7:
            params = get_params(opcode, prog, prog[ip+1:ip+4], modes)
            if params[0] < params[1]:
                prog[params[2]] = 1
            else:
                prog[params[2]] = 0

        elif opcode == 8:
            params = get_params(opcode, prog, prog[ip+1:ip+4], modes)
            if params[0] == params[1]:
                prog[params[2]] = 1
            else:
                prog[params[2]] = 0

        if not ipset:
            ip += len(params) + 1

    return OUTPUT

amplifiers = permutations([0, 1, 2, 3, 4])

vals = []
for amp in amplifiers:
    OUTPUT = 0
    for INPUT in amp:
        prog = original.copy()
        OUTPUT = run_program(prog, [INPUT, OUTPUT])

    vals.append(OUTPUT)

print(max(vals))
