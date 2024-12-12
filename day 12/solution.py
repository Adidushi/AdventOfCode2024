import cv2
import numpy as np


def flood_fill(grid: dict[complex, str], position: complex, visited: set[complex]) \
        -> tuple[int, int, set[complex]]:
    group = set()
    group.add(position)
    visited.add(position)
    perimeter = 4
    area = 1
    for direction in (1, -1, 1j, -1j):
        new_position = position + direction
        if new_position not in grid or grid[position] != grid[new_position]:
            continue
        elif new_position in visited:
            perimeter -= 1
        else:
            new_p, new_a, points = flood_fill(grid, new_position, visited)
            perimeter += new_p - 1
            area += new_a
            group = group.union(points)
    return perimeter, area, group


def grid_iterator(grid):
    pos = 0
    while pos in grid:
        yield pos
        if pos + 1 in grid:
            pos += 1
            continue
        im = pos.imag
        pos = (im + 1) * 1j


def q1():
    grid = dict()
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        for row, line in enumerate(data):
            for col, ch in enumerate(line):
                pos = col + 1j * row
                grid[pos] = ch

    groups = list()
    visited = set()
    total = 0
    for pos in grid_iterator(grid):
        if pos not in visited:
            perimeter, area, group = flood_fill(grid, pos, visited)
            total += perimeter * area
            groups.append((group, perimeter, area))
    return total


def complex_list_to_array(group: set[complex]):
    min_x = min(n.real for n in group)
    max_x = max(n.real for n in group)
    min_y = min(n.imag for n in group)
    max_y = max(n.imag for n in group)
    width = int(max_x - min_x) + 1
    height = int(max_y - min_y) + 1

    image = list()

    for w in range(-1, width + 1):
        line = list()
        for h in range(-1, height + 1):
            if (w + min_x + (h + min_y) * 1j) in group:
                line.append((255, 255, 255))
            else:
                line.append((0, 0, 0))
        image.append(line)

    return image


def count_corners(group):
    corners = 0
    for point in group:
        tl = point - 1 - 1j
        tr = point + 1 - 1j
        bl = point - 1 + 1j
        br = point + 1 + 1j
        u = point - 1j
        d = point + 1j
        l = point - 1
        r = point + 1
        corners += l not in group and u not in group
        corners += r not in group and u not in group
        corners += l not in group and d not in group
        corners += r not in group and d not in group
        corners += l in group and u in group and tl not in group
        corners += r in group and u in group and tr not in group
        corners += l in group and d in group and bl not in group
        corners += r in group and d in group and br not in group
    return corners


def q2():
    grid = dict()
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        for row, line in enumerate(data):
            for col, ch in enumerate(line):
                pos = col + 1j * row
                grid[pos] = ch

    visited = set()
    total = 0
    for pos in grid_iterator(grid):
        if pos not in visited:
            perimeter, area, group = flood_fill(grid, pos, visited)
            total += count_corners(group) * area

    return total


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
