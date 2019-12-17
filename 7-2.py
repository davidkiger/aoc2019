from collections import deque
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


class WaitingForInput(Exception):
    pass


class OutputSent(Exception):
    pass


class Machine:
    def __init__(self):
        self.prog = original.copy()
        self.ip = 0
        self.inputs = deque()
        self.outputs = deque()
        self.done = False

    def add_input(self, val):
        self.inputs.append(val)

    def get_output(self):
        return self.outputs.popleft()

    def run(self):
        while True:
            digits = list(map(int, str(self.prog[self.ip])))
            opcode = digits[-1]
            if len(digits) > 1:
                opcode += digits[-2]*10
            modes = digits[:-2]
            modes = modes[::-1]

            # print(opcode)
            if opcode == 1:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+4], modes)
                self.prog[params[2]] = params[0] + params[1]
                self.ip += 4

            elif opcode == 2:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+4], modes)
                self.prog[params[2]] = params[0] * params[1]
                self.ip += 4

            elif opcode == 3:
                try:
                    params = [self.prog[self.ip+1]]
                    self.prog[params[0]] = self.inputs.popleft()
                    self.ip += 2
                except(IndexError):
                    raise WaitingForInput

            elif opcode == 4:
                params = [self.prog[self.ip+1]]
                self.outputs.append(self.prog[params[0]])
                self.ip += 2
                raise OutputSent

            elif opcode == 5:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+3], modes)
                if params[0] != 0:
                    self.ip = params[1]
                else:
                    self.ip += 3

            elif opcode == 6:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+3], modes)
                if params[0] == 0:
                    self.ip = params[1]
                else:
                    self.ip += 3

            elif opcode == 7:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+4], modes)
                if params[0] < params[1]:
                    self.prog[params[2]] = 1
                else:
                    self.prog[params[2]] = 0
                self.ip += 4

            elif opcode == 8:
                params = get_params(opcode, self.prog, self.prog[self.ip+1:self.ip+4], modes)
                if params[0] == params[1]:
                    self.prog[params[2]] = 1
                else:
                    self.prog[params[2]] = 0
                self.ip += 4

            elif opcode == 99:
                self.done = True
                return

amp_orders = permutations([5, 6, 7, 8, 9])

def test_perm(p):
    amps = list()
    for phase in p:
        amps.append(Machine())
        amps[-1].add_input(phase)

    m = 0
    amps[0].add_input(0)
    while (True):
        while (not amps[m].done):
            next_m = (m+1) % 5
            try:
                amps[m].run()
            except(OutputSent):
                amps[next_m].add_input(amps[m].outputs[-1])
            except(WaitingForInput):
                break

        m = next_m

        if (all(m.done for m in amps)):
            break

    return amps[0].inputs[-1]

vals = []
for order in amp_orders:
    vals.append(test_perm(order))

print(max(vals))
