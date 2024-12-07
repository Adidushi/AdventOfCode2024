def check_index(i, j, text, word):
    c = 0
    if j + len(word) - 1 < len(text[0]):
        if text[i][j:j + 4] == word:
            c += 1

    if i + len(word) - 1 < len(text):
        vertical = ''
        for k in range(4):
            vertical += text[i + k][j]
        if vertical == word:
            c += 1

    if i + len(word) - 1 < len(text) and j + len(word) - 1 < len(text[0]):
        diag = ''
        for k in range(4):
            diag += text[i + k][j + k]
        if diag == word:
            c += 1

    if i + len(word) - 1 < len(text) and j - len(word) + 1 >= 0:
        diag = ''
        for k in range(4):
            diag += text[i + k][j - k]
        if diag == word:
            c += 1

    return c


def crossmas(i, j, text, word):
    x1, x2, x3 = word

    if ((text[i][j] == x1 and
         text[i + 1][j + 1] == x2 and
         text[i + 2][j + 2] == x3) and
            ((text[i + 2][j] == x1 and
              text[i][j + 2] == x3) or
             (text[i + 2][j] == x3 and
              text[i][j + 2] == x1))):
        return 1
    return 0


def q1():
    t = 0
    with open('input.txt') as f:
        content = f.read().splitlines()
        for i in range(len(content)):
            for j in range(len(content[0])):
                t += check_index(i, j, content, 'XMAS')
                t += check_index(i, j, content, 'SAMX')

    return t


def q2():
    t = 0
    with open('input.txt') as f:
        content = f.read().splitlines()
        for i in range(len(content) - 2):
            for j in range(len(content[0]) - 2):
                t += crossmas(i, j, content, 'MAS')
                t += crossmas(i, j, content, 'SAM')

    return t


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
