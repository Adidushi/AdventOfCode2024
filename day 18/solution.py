from collections import deque


def q1(samples=1034):
    size = 70
    with open('input.txt', 'r') as f:
        data = [complex(int(x), int(y)) for x, y in [line.split(',') for line in f.read().splitlines()]]
    grid = {complex(x, y): '.' for x in range(size + 1) for y in range(size + 1)}
    for point in data[:samples]:
        grid[point] = '#'
    queue = deque()
    queue.append((0, 0))
    visited = set()
    while queue:
        current_position, length = queue.popleft()
        if current_position == complex(size, size):
            return length
        neighbors = {current_position + 1, current_position - 1, current_position + 1j, current_position - 1j}
        for neighbor in neighbors:
            if (neighbor not in visited) and (grid.get(neighbor) == '.'):
                visited.add(neighbor)
                queue.append((neighbor, length + 1))


def q2():
    with open('input.txt', 'r') as f:
        data = [complex(int(x), int(y)) for x, y in [line.split(',') for line in f.read().splitlines()]]
    for x in range(1025, 3451):
        if q1(x) is None:
            return f'{int(data[x - 1].real)},{int(data[x - 1].imag)}'


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
