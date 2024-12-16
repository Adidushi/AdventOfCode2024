import heapq
from dataclasses import dataclass


@dataclass
class State:
    cost: int
    position: complex
    direction: complex | None

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost


def bfs(grid, start, end):
    bfs_memory = dict()

    queue = [State(0, start, None)]
    heapq.heapify(queue)

    while queue:
        state: State = heapq.heappop(queue)
        if state.position in bfs_memory:
            bfs_memory[state.position] = min(bfs_memory[state.position], state.cost)
        else:
            bfs_memory[state.position] = state.cost

        directions = [i for i in {1, -1, 1j, -1j} if grid[state.position + i] != '#']
        for direction in directions:
            if state.position + direction in bfs_memory and state.cost >= bfs_memory[state.position + direction]:
                continue
            next_cost = 1 if state.direction == direction else 1001
            heapq.heappush(queue, State(state.cost + next_cost, state.position + direction, direction))

    return bfs_memory[end]


def q1():
    with open('input.txt', 'r') as f:
        positions = f.read().splitlines()

    grid = dict()
    start_position = 0
    end_position = 0
    for y, line in enumerate(positions):
        for x, char in enumerate(line):
            if char == 'S':
                start_position = complex(x, y)
                char = '.'
            elif char == 'E':
                end_position = complex(x, y)
                char = '.'
            grid[complex(x, y)] = char
    return bfs(grid, start_position, end_position)


@dataclass
class State2:
    cost: int
    position: complex
    direction: complex | None
    path: tuple[complex]

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost


def bfs_paths(grid, start, end):
    queue = [State2(0, start, None, (start,))]
    heapq.heapify(queue)

    end_paths = list()

    min_cost_per_tile = dict()

    while queue:
        state: State2 = heapq.heappop(queue)
        if state.position == end:
            end_paths.append((state.cost, state.path))
        if state.cost >= min_cost_per_tile.get(end, state.cost+1):
            continue
        directions = [i for i in {1, -1, 1j, -1j} if grid[state.position + i] != '#']
        for direction in directions:
            next_position = state.position + direction
            if next_position in state.path:
                continue
            next_cost = (1 if state.direction == direction else 1001) + state.cost
            if next_position in min_cost_per_tile and min_cost_per_tile[next_position] < next_cost:
                continue
            heapq.heappush(queue, State2(next_cost, next_position, direction, state.path + (next_position,)))

    tiles = set()
    min_cost = min(cost for cost, path in end_paths)
    for cost, path in end_paths:
        if cost == min_cost:
            tiles = tiles.union(path)
    return len(tiles)


def print_grid(grid, path_tiles):
    pos = 0
    while True:
        if pos in path_tiles:
            print('O', end='')
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


def q2():
    with open('input.txt', 'r') as f:
        positions = f.read().splitlines()

    grid = dict()
    start_position = 0
    end_position = 0
    for y, line in enumerate(positions):
        for x, char in enumerate(line):
            if char == 'S':
                start_position = complex(x, y)
            elif char == 'E':
                end_position = complex(x, y)
            grid[complex(x, y)] = char
    return bfs_paths(grid, start_position, end_position)


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
