def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    grid = dict()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            pos = col + row * 1j
            grid[pos] = int(char)

    total = 0
    for pos, height in grid.items():
        if height != 0:
            continue
        total += accessibles(grid, pos)
    return total


def accessibles(grid, pos):
    curr_nodes = set()
    curr_nodes.add(pos)
    next_nodes = set()
    for height in range(1, 10):
        for node in curr_nodes:
            for new_pos in (node + 1, node - 1, node + 1j, node - 1j):
                if new_pos in grid and grid[new_pos] == height:
                    next_nodes.add(new_pos)

        curr_nodes, next_nodes = next_nodes, set()
    return len(curr_nodes)


def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    grid = dict()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            pos = col + row * 1j
            grid[pos] = int(char)

    initials = {(pos,) for pos, height in grid.items() if height == 0}
    return paths(grid, initials)


def paths(grid, curr_paths):
    next_paths = set()
    for height in range(1, 10):
        for path in curr_paths:
            node = path[-1]
            for new_pos in (node + 1, node - 1, node + 1j, node - 1j):
                if new_pos in grid and grid[new_pos] == height:
                    next_paths.add(path + (new_pos,))

        curr_paths, next_paths = next_paths, set()
    return len(curr_paths)


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
