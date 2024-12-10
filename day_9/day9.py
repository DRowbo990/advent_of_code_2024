import numpy as np

blocks = np.array([int(z) for z in open("input.txt").read()])
locs = np.cumsum(blocks)
locs = np.insert(locs, 0, 0)

mem = np.array([-1] * np.sum(blocks))
for ind in range(0, len(locs), 2):
    val = ind // 2
    for l in range(locs[ind], locs[ind + 1]):
        mem[l] = val
spaces = np.nonzero(mem == -1)[0]
vals = np.flip(np.nonzero(mem != -1)[0][-len(spaces) :])
mem[spaces] = mem[vals]

print(np.sum(mem[: -len(spaces)] * np.arange(0, len(mem) - len(spaces))))
