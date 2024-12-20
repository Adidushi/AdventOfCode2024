from collections import deque
from itertools import combinations


def print_grid(grid, distance_grid):
    pos = 0
    while True:
        if pos in distance_grid:
            print(str(distance_grid[pos] % 10), end='')
        else:
            print(grid[pos], end='')
        if (pos + 1) in grid:
            pos += 1
        elif (pos.imag + 1) * 1j in grid:
            pos = (pos.imag + 1) * 1j
            print('')
        else:
            break
    print()


def q1():
    grid = dict()
    start = 0
    end = 0
    with open('input.txt', 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                if char == 'S':
                    start = complex(x, y)
                if char == 'E':
                    end = complex(x, y)
                grid[complex(x, y)] = char

    distance_grid = dict()
    visited = set()
    next_pos = position = start
    distance = 0
    while position != end:
        position = next_pos
        distance_grid[position] = distance
        visited.add(position)
        next_pos = next((neighbor for neighbor in {position + 1, position - 1, position + 1j, position - 1j} if
                         neighbor in grid and neighbor not in visited and grid[neighbor] != '#'), None)

        distance += 1
    count = 0
    for position, position_distance in distance_grid.items():
        for skip_position in {position + 2, position - 2, position + 2j, position - 2j,
                              position + 1 + 1j, position - 1 - 1j, position + 1 - 1j, position - 1 + 1j}:
            if skip_position not in distance_grid:
                continue
            if (distance_grid[skip_position] - position_distance) - 2 >= 100:
                count += 1

    return count


def q2():
    grid = dict()
    start = 0
    end = 0
    with open('input.txt', 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                if char == 'S':
                    start = complex(x, y)
                if char == 'E':
                    end = complex(x, y)
                grid[complex(x, y)] = char

    distance_grid = dict()
    visited = set()
    next_pos = position = start
    distance = 0
    while position != end:
        position = next_pos
        distance_grid[position] = distance
        visited.add(position)
        next_pos = next((neighbor for neighbor in {position + 1, position - 1, position + 1j, position - 1j} if
                         neighbor in grid and neighbor not in visited and grid[neighbor] != '#'), None)

        distance += 1

    count = 0
    for (pos1, pos1_dist), (pos2, pos2_dist) in combinations(distance_grid.items(), 2):
        point_dist = abs(pos1.real - pos2.real) + abs(pos1.imag - pos2.imag)
        if point_dist <= 20 and pos2_dist - pos1_dist - point_dist >= 100:
            count += 1

    return count


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
