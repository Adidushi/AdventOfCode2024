def evolve_stone(stone, iterations, cache):
    if (stone, iterations) in cache:
        return cache[(stone, iterations)]

    if iterations == 0:
        return 1

    if stone == 0:
        cache[(stone, iterations)] = evolve_stone(1, iterations - 1, cache)
        return cache[(stone, iterations)]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        left_stone = int(stone_str[:len(stone_str) // 2])
        right_stone = int(stone_str[len(stone_str) // 2:])
        cache[(stone, iterations)] = (evolve_stone(left_stone, iterations - 1, cache) +
                                      evolve_stone(right_stone, iterations - 1, cache))
        return cache[(stone, iterations)]
    cache[(stone, iterations)] = evolve_stone(stone * 2024, iterations - 1, cache)
    return cache[(stone, iterations)]


def q1():
    with open('input.txt', 'r') as f:
        stones = [int(n) for n in f.read().split()]
    cache = dict()
    return sum(evolve_stone(stone, 25, cache) for stone in stones)


def q2():
    with open('input.txt', 'r') as f:
        stones = [int(n) for n in f.read().split()]
    cache = dict()
    return sum(evolve_stone(stone, 75, cache) for stone in stones)


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
