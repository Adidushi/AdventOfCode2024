import re
from dataclasses import dataclass


@dataclass
class ClawMachine:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int


def parse(data: list[list[str]], part2=False) -> list[ClawMachine]:
    machines = list()
    bonus = 10000000000000 if part2 else 0
    for group in data:
        a, b, prize = group
        a_x, a_y = map(int, re.findall(r'(?<=\+)\d+', a))
        b_x, b_y = map(int, re.findall(r'(?<=\+)\d+', b))
        prize_x, prize_y = map(int, re.findall(r'(?<==)\d+', prize))
        machines.append(ClawMachine(a_x, a_y, b_x, b_y, prize_x + bonus, prize_y + bonus))
    return machines


def q1():
    with open('input.txt', 'r') as f:
        data = [group.splitlines() for group in f.read().split('\n\n')]
    machines = parse(data)
    tokens = 0
    for m in machines:
        a_presses = (m.prize_y * m.b_x - m.prize_x * m.b_y) / (m.b_x * m.a_y - m.a_x * m.b_y)
        b_presses = (m.prize_y * m.a_x - m.prize_x * m.a_y) / (m.a_x * m.b_y - m.b_x * m.a_y)
        if a_presses == int(a_presses) and b_presses == int(b_presses) and a_presses <= 100 and b_presses <= 100:
            tokens += int((3 * a_presses + b_presses))
    return tokens


def q2():
    with open('input.txt', 'r') as f:
        data = [group.splitlines() for group in f.read().split('\n\n')]
    machines = parse(data, part2=True)
    tokens = 0
    for m in machines:
        a_presses = (m.prize_y * m.b_x - m.prize_x * m.b_y) / (m.b_x * m.a_y - m.a_x * m.b_y)
        b_presses = (m.prize_y * m.a_x - m.prize_x * m.a_y) / (m.a_x * m.b_y - m.b_x * m.a_y)
        if a_presses == int(a_presses) and b_presses == int(b_presses):
            tokens += int((3 * a_presses + b_presses))
    return tokens


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
