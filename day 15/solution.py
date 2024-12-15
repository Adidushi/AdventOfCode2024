from typing import Optional

directions = {
    '<': complex(-1, 0),
    '^': complex(0, -1),
    '>': complex(1, 0),
    'v': complex(0, 1),
}
inv_directions = {v: k for k, v in directions.items()}

WALL = '#'
BOX = 'O'
EMPTY = '.'


def print_grid(grid, bot_pos):
    pos = 0
    while True:
        if pos == bot_pos:
            print('@', end='')
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


def check_boxes(grid, box_position, command) -> Optional[complex]:
    while grid[box_position] == BOX:
        box_position += command
    if grid[box_position] == WALL:
        return None
    return box_position


def q1():
    with open('input.txt', 'r') as f:
        positions, commands_str = f.read().split('\n\n')
    positions = positions.splitlines()
    commands: list[complex] = [directions[c] for c in commands_str.replace('\n', '')]

    grid = dict()
    position = 0
    for y, line in enumerate(positions):
        for x, char in enumerate(line):
            if char == '@':
                position = complex(x, y)
                char = '.'
            grid[complex(x, y)] = char

    for command in commands:
        next_position = position + command
        if grid[next_position] == WALL:
            continue
        if grid[next_position] == EMPTY:
            position = next_position
            continue
        if grid[next_position] == BOX:
            free_space = check_boxes(grid, next_position, command)
            if free_space is None:
                continue
            grid[free_space] = BOX
            grid[next_position] = EMPTY
            position = next_position
    return sum(int(100 * pos.imag) + int(pos.real) for pos, val in grid.items() if val == BOX)


second_char = {
    '#': '#',
    '@': '.',
    '.': '.',
    '[': ']'
}
HORIZONTAL = {1, -1}


def check_boxes_2(grid, box_position, command, boxes: set[tuple[str, complex]]) -> bool:
    if grid[box_position] == '[':
        box_left, box_right = box_position, box_position + 1
    else:
        box_left, box_right = box_position - 1, box_position
    boxes.add(('[', box_left))
    boxes.add((']', box_right))
    if command in HORIZONTAL:
        if command == 1:
            if grid[box_right + 1] == EMPTY:
                return True
            elif grid[box_right + 1] in '[]':
                return check_boxes_2(grid, box_right + 1, command, boxes)
            elif grid[box_right + 1] == WALL:
                return False

        if command == -1:
            if grid[box_left - 1] == EMPTY:
                return True
            elif grid[box_left - 1] in '[]':
                return check_boxes_2(grid, box_left - 1, command, boxes)
            elif grid[box_left - 1] == WALL:
                return False
    else:
        if grid[box_left + command] == EMPTY and grid[box_right + command] == EMPTY:
            return True

        if grid[box_left + command] == EMPTY and grid[box_right + command] in '[]':
            return check_boxes_2(grid, box_right + command, command, boxes)

        if grid[box_left + command] in '[]' and grid[box_right + command] == EMPTY:
            return check_boxes_2(grid, box_left + command, command, boxes)

        if grid[box_left + command] in '[]' and grid[box_right + command] in '[]':
            return (check_boxes_2(grid, box_left + command, command, boxes) and
                    check_boxes_2(grid, box_right + command, command, boxes))

        if grid[box_left + command] == WALL or grid[box_right + command] == WALL:
            return False


def q2():
    with open('input.txt', 'r') as f:
        positions, commands_str = f.read().split('\n\n')
    positions = positions.splitlines()
    commands: list[complex] = [directions[c] for c in commands_str.replace('\n', '')]

    grid = dict()
    position = 0
    for y, line in enumerate(positions):
        for x, char in enumerate(line):
            if char == BOX:
                char = '['
            if char == '@':
                position = complex(2 * x, y)
                char = '.'
            grid[complex(2 * x, y)] = char
            grid[complex(2 * x + 1, y)] = second_char[char]

    for command in commands:

        next_position = position + command
        if grid[next_position] == WALL:
            continue
        if grid[next_position] == EMPTY:
            position = next_position
            continue
        if grid[next_position] in '[]':
            boxes_to_move = set()
            free_space = check_boxes_2(grid, next_position, command, boxes_to_move)
            if not free_space:
                continue

            # remove old boxes
            for box_side, box_position in boxes_to_move:
                grid[box_position] = EMPTY

            # add new boxes
            for box_side, box_position in boxes_to_move:
                grid[box_position + command] = box_side
            position = next_position

    return sum(int(100 * pos.imag) + int(pos.real) for pos, val in grid.items() if val == '[')


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
