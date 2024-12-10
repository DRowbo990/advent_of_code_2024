import numpy as np

blocks = np.array([int(z) for z in open("input.txt").read()])

locs = np.cumsum(blocks)  # get the starting address of each block
locs = np.insert(locs, 0, 0)

spaces = [
    np.arange(locs[i], locs[i + 1]) for i in range(1, len(locs) - 1, 2)
]  # addresses of spaces
space_lens = blocks[1::2]  # lengths of empty memory chunks left

files = [
    np.arange(locs[i], locs[i + 1]) for i in range(len(locs) - 2, 0, -2)
]  # addresses of files starting from the right
file_lens = [len(f) for f in files]  # file lengths

mem = np.zeros(np.sum(blocks), dtype=np.int16)  # initialize memory
for ind in range(0, len(locs), 2):
    val = ind // 2
    for l in range(locs[ind], locs[ind + 1]):
        mem[l] = val

file_num, space_num = len(files), len(spaces)

for j in range(file_num):  # loop through the files
    valids = [
        i
        for i in range(space_num)
        if file_lens[j] <= space_lens[i] and spaces[i][-1] < files[j][0]
    ]  # get the leftmost valid space
    if len(valids) > 0:  # if such a space exists
        space = min(valids)  # get the leftmost one
        spaces_put = spaces[space][
            : file_lens[j]
        ]  # only select the needed sub-portion of space
        spaces[space] = spaces[space][file_lens[j] :]  # update free space left
        space_lens[space] -= file_lens[j]  # update the length of this chunk of space
        mem[spaces_put] = mem[files[j]]  # copy the file
        mem[files[j]] = 0  # delete the file

print(np.sum(mem * np.arange(0, len(mem))))
