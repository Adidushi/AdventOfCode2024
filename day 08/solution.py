import itertools
import math

def q1():
    antennae_frequencies = dict()
    anti_nodes = set()
    grid = dict()
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
        for j, line in enumerate(input):
            for i, ch in enumerate(line):
                coord = complex(i, j)
                grid[coord] = ch
                if ch == '.':
                    continue
                if ch not in antennae_frequencies:
                    antennae_frequencies[ch] = set()
                antennae_frequencies[ch].add(coord)

    for freq, antennae in antennae_frequencies.items():
        for c1, c2 in itertools.permutations(antennae, 2):
            vec = c2-c1
            anti_node = c2+vec
            if anti_node in grid:
                anti_nodes.add(anti_node)

    return len(anti_nodes)

def q2():
    antennae_frequencies = dict()
    anti_nodes = set()
    grid = dict()
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
        for j, line in enumerate(input):
            for i, ch in enumerate(line):
                coord = complex(i, j)
                grid[coord] = ch
                if ch == '.':
                    continue
                if ch not in antennae_frequencies:
                    antennae_frequencies[ch] = set()
                antennae_frequencies[ch].add(coord)

    for freq, antennae in antennae_frequencies.items():
        for c1, c2 in itertools.permutations(antennae, 2):
            vec = c2 - c1
            gcd = math.gcd(int(vec.real), int(vec.imag))
            vec /= gcd
            anti_node = c2
            while anti_node in grid:
                anti_nodes.add(anti_node)
                anti_node += vec

    return len(anti_nodes)


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