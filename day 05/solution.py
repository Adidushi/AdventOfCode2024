from graphlib import TopologicalSorter


def check_update(update, graph):
    g = dict()
    for k, vl in graph.items():
        if k in update:
            g[k] = [v for v in vl if v in update]
    toposort = tuple(reversed(tuple(TopologicalSorter(g).static_order())))
    uidx = 0
    for n in toposort:
        if update[uidx] == n:
            uidx += 1
            if uidx >= len(update):
                return update[uidx // 2]
    return update[uidx // 2] if uidx == len(update) else 0


def add_new(update, graph):
    g = dict()
    for k, vl in graph.items():
        if k in update:
            g[k] = [v for v in vl if v in update]
    toposort = tuple(reversed(tuple(TopologicalSorter(g).static_order())))
    return toposort[len(toposort) // 2]


def q1():
    with open('input.txt', 'r') as f:
        orders, updates = f.read().split('\n\n')
    g = dict()
    for line in orders.splitlines():
        pre, post = map(int, line.split('|'))
        if pre not in g:
            g[pre] = set()
        g[pre].add(post)

    update_list = list()
    for update in updates.splitlines():
        update_list.append([int(u) for u in update.split(',')])

    return sum([check_update(update, g) for update in update_list])


def q2():
    with open('input.txt', 'r') as f:
        orders, updates = f.read().split('\n\n')
    g = dict()
    for line in orders.splitlines():
        pre, post = map(int, line.split('|'))
        if pre not in g:
            g[pre] = set()
        g[pre].add(post)

    update_list = list()
    for update in updates.splitlines():
        update_list.append([int(u) for u in update.split(',')])

    s = 0
    for update in update_list:
        if check_update(update, g) == 0:
            s += add_new(update, g)

    return s


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
