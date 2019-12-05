file = open("2-1.in", "r")

for line in file:
    original = list(map(int, line.strip().split(',')))

halt = 19690720
for noun in range(0, 100):
    for verb in range(noun, 100):
        prog = original.copy()
        ip = 0
        prog[1] = noun
        prog[2] = verb

        while(prog[ip] != 99):
            if prog[ip] == 1:
                params = (prog[ip+1], prog[ip+2], prog[ip+3])
                prog[params[2]] = prog[params[0]] + prog[params[1]]
            elif prog[ip] == 2:
                params = (prog[ip+1], prog[ip+2], prog[ip+3])
                prog[params[2]] = prog[params[0]] * prog[params[1]]
            ip += len(params) + 1

        if (prog[0] == halt):
            print('{}{}'.format(noun, verb))
