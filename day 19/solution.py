from functools import cache


@cache
def is_possible(towel, available_towels):
    if towel == '':
        return 1
    total_ways = 0
    for starter in available_towels:
        if towel.startswith(starter):
            remaining = towel[len(starter):]
            total_ways += is_possible(remaining, available_towels)
    return total_ways


def q1():
    with open('input.txt', 'r') as f:
        available_towels, wanted_towels = f.read().split('\n\n')
        available_towels = tuple(available_towels.split(', '))
        wanted_towels = wanted_towels.splitlines()
    return sum(1 if is_possible(towel, available_towels) else 0 for towel in wanted_towels)


def q2():
    with open('input.txt', 'r') as f:
        available_towels, wanted_towels = f.read().split('\n\n')
        available_towels = tuple(available_towels.split(', '))
        wanted_towels = wanted_towels.splitlines()
    return sum(is_possible(towel, available_towels) for towel in wanted_towels)


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
