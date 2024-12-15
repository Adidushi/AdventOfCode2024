dirs = {
    '^': 0 - 1j,
    'v': 0 + 1j,
    '>': 1,
    '<': -1
}
next_dirs = {
    '^': '>',
    'v': '<',
    '>': 'v',
    '<': '^'
}


def print_grid(grid):
    pos = 0
    while True:
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
    pos = 0
    direction = ''
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            for j, ch in enumerate(line):
                grid[j + 1j * i] = ch
                if ch not in '#.':
                    pos = j + 1j * i
                    direction = ch
                    grid[j + 1j * i] = '.'

    counter = 0
    while pos in grid:
        if grid[pos] == '.':
            counter += 1
            grid[pos] = 'X'
        next_pos = pos + dirs[direction]
        if next_pos in grid and grid[next_pos] == '#':
            direction = next_dirs[direction]
            continue
        pos = pos + dirs[direction]

    return counter


def q2():
    grid = dict()
    pos = 0
    initial = 0
    direction = ''
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            for j, ch in enumerate(line):
                grid[j + 1j * i] = ch
                if ch not in '#.':
                    pos = j + 1j * i
                    initial = pos
                    direction = ch
                    grid[j + 1j * i] = '.'
    positions = set()
    while pos in grid:
        if grid[pos] == '.' and pos not in positions:
            positions.add(pos)
        next_pos = pos + dirs[direction]
        if next_pos in grid and grid[next_pos] == '#':
            direction = next_dirs[direction]
            continue
        pos = pos + dirs[direction]

    possible = set()
    for pos in positions:
        grid[pos] = '#'
        if check_loop(initial, grid):
            possible.add(pos)
        grid[pos] = '.'
    return len(possible)


def check_loop(pos, grid):
    direction = '^'

    positions = set()
    inarow = 0
    while pos in grid:
        next_pos = pos + dirs[direction]
        if pos in positions:
            inarow += 1
        else:
            inarow = 0
        if inarow == 300:
            return True
        if grid[pos] == '.' and pos not in positions:
            positions.add(pos)
        if next_pos in grid and grid[next_pos] == '#':
            direction = next_dirs[direction]
            continue
        pos = pos + dirs[direction]
    return False


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
