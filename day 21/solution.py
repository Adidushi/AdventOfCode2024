from collections import deque
from functools import cache

num_pad = {c: (row, col) for
           row, line in enumerate('789\n456\n123\n 0A'.splitlines())
           for col, c in enumerate(line) if c != ' '}

arrow_pad = {c: (row, col) for
             row, line in enumerate(' ^A\n<v>'.splitlines())
             for col, c in enumerate(line) if c != ' '}
pads = {
    len(num_pad): num_pad,
    len(arrow_pad): arrow_pad
}


def get_sequence(pad, start, end):
    queue = deque()
    queue.append((start, ''))
    while queue:
        current_position, path = queue.pop()

        target_pos = pad[end]
        if current_position == pad[end]:
            yield path
            continue

        column_move = target_pos[1] - current_position[1]
        if column_move != 0:
            new_point = current_position[0], current_position[1] + (column_move // abs(column_move))
            if new_point in pad.values():
                if column_move > 0:
                    queue.append((new_point, path + '>'))
                elif column_move < 0:
                    queue.append((new_point, path + '<'))

        row_move = target_pos[0] - current_position[0]
        if row_move != 0:
            new_point = current_position[0] + (row_move // abs(row_move)), current_position[1]
            if new_point in pad.values():
                if row_move > 0:
                    queue.append((new_point, path + 'v'))
                elif row_move < 0:
                    queue.append((new_point, path + '^'))


@cache
def get_shortest_instructions(pad_len, code, num_bots):
    pad = pads[pad_len]
    if num_bots == 0:
        return len(code)

    current_pos = pad['A']
    min_length = 0

    for letter in code:
        min_length += min(
            get_shortest_instructions(len(arrow_pad), sequence + 'A', num_bots - 1)
            for sequence in get_sequence(pad, current_pos, letter))

        current_pos = pad[letter]

    return min_length


def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    total = 0
    for code in data:
        total += int(code[:-1]) * get_shortest_instructions(len(num_pad), code, 3)
    return total


def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    total = 0
    for code in data:
        total += int(code[:-1]) * get_shortest_instructions(len(num_pad), code, 26)
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
