def q1():
    with open('input.txt', 'r') as f:
        content = f.read()
    idx = 0
    memory = list()
    empty = False
    for c in map(int, content):
        for _ in range(c):
            memory.append(-1 if empty else idx)
        empty = not empty
        idx += 1 if not empty else 0

    s = 0
    while s < len(memory):
        if memory[s] != -1:
            s += 1
            continue
        if memory[-1] == -1:
            memory.pop()
            continue
        memory[s] = memory.pop()

    return sum([i * n for i, n in enumerate(memory)])


def q2():
    with open('input.txt', 'r') as f:
        content = f.read()
    idx = 0
    cnt = 0
    empty = False
    memory = list()
    for c in map(int, content):
        memory.append((idx if not empty else -1, c))
        empty = not empty
        idx += 1 if not empty else 0
        cnt += 1

    minnum = memory[-1][0]

    while minnum > 0:
        for i, o in enumerate(memory):
            if o[0] == minnum:
                minnum_index = i
        val, length = memory[minnum_index]

        possible = findspot(memory, minnum_index)
        if possible is not None:
            possible_val, possible_length = memory[possible]
            if length == possible_length:
                memory[possible] = (val, possible_length)
                memory[minnum_index] = (-1, length)
            elif possible_length > length:
                memory[possible] = (val, length)
                memory[minnum_index] = (-1, length)
                memory.insert(possible + 1, (-1, possible_length - length))
        minnum -= 1

    stmem = list()
    for v, l in memory:
        for _ in range(l):
            v = 0 if v == -1 else v
            stmem.append(v)
    return sum([i * n for i, n in enumerate(stmem)])


def findspot(memory, i):
    val, length = memory[i]

    for j in range(i):
        jval, jlen = memory[j]
        if jval == -1 and jlen >= length:
            return j


if __name__ == '__main__':
    from time import perf_counter as pc

    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1 - st) * 1000}ms\n\
            Part 2: {(pt2 - pt1) * 1000}ms\n\
            Total: {(pt2 - st) * 1000}ms')
