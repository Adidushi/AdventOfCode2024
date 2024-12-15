def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    l1, l2 = zip(*[(int(line.split()[0]), int(line.split()[-1])) for line in data])
    t = 0
    for p1, p2 in zip(sorted(l1), sorted(l2)):
        t += abs(p1 - p2)
    return t


def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    l1, l2 = zip(*[(int(line.split()[0]), int(line.split()[-1])) for line in data])
    t = 0
    for p1 in l1:
        t += l2.count(p1) * p1
    return t


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
