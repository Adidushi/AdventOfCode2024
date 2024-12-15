from typing import List


def check_report(rep: List[int]):
    rising = None
    for prev, curr in zip(rep, rep[1:]):
        if rising is None:
            rising = True if prev < curr else False
        if prev > curr and rising or prev < curr and not rising:
            return 0
        diff = abs(prev - curr)
        if not (1 <= diff <= 3):
            return 0
    return 1


def check_tolerate(rep: List[int]):
    if check_report(rep):
        return 1
    for j in range(len(rep)):
        if check_report(rep[:j] + rep[j + 1:]):
            return 1
    return 0


def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return sum(check_report(list(map(int, r.split()))) for r in data)


def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return sum(check_tolerate(list(map(int, r.split()))) for r in data)


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
