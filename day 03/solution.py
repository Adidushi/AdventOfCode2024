import math
import re


def q1():
    with open('input.txt', 'r') as f:
        return sum(math.prod(map(int, m)) for m in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', f.read()))


def q2():
    with open('input.txt', 'r') as f:
        t = 0
        do = True
        for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', f.read()):
            if m.group(3):
                do = True
            elif m.group(4):
                do = False
            elif do:
                t += math.prod(map(int, m.groups()[:2]))
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
