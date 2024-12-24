def eval_label(label, operations, initials):
    if label in initials:
        return initials[label]
    l1, l2, op = operations[label]

    match op:
        case 'OR':
            return eval_label(l1, operations, initials) or eval_label(l2, operations, initials)
        case 'AND':
            return eval_label(l1, operations, initials) and eval_label(l2, operations, initials)
        case 'XOR':
            return eval_label(l1, operations, initials) != eval_label(l2, operations, initials)


def q1():
    with open('input.txt', 'r') as f:
        inputs, relations = f.read().split('\n\n')
        inputs = inputs.splitlines()
        relations = relations.splitlines()

    initials = dict()
    for line in inputs:
        label, val = line.split(': ')
        initials[label] = bool(int(val))

    outputs = set()
    operations = dict()
    for line in relations:
        ins, out = line.split(' -> ')
        l1, op, l2 = ins.split()
        operations[out] = (l1, l2, op)
        if out[0] == 'z':
            outputs.add(out)

    out_num = ''
    for output in sorted(outputs, reverse=True):
        val = eval_label(output, operations, initials)
        out_num += '1' if val else '0'

    return int(out_num, 2)


def eval_label_path(label, operations, initials):
    if label in initials:
        return initials[label]

    l1, l2, op = operations[label]

    match op:
        case 'OR':
            return eval_label(l1, operations, initials) or eval_label(l2, operations, initials)
        case 'AND':
            return eval_label(l1, operations, initials) and eval_label(l2, operations, initials)
        case 'XOR':
            return eval_label(l1, operations, initials) != eval_label(l2, operations, initials)

def q2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()


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
