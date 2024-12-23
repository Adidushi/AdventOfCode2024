import itertools

import networkx as nx
import matplotlib.pyplot as plt


def q1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    t_nodes = set()
    edges = set()
    for line in data:
        n1, n2 = line.split('-')
        for n in (n1, n2):
            if n[0] == 't':
                t_nodes.add(n)
        edges.add((n1, n2))

    g = nx.Graph()
    g.add_edges_from(edges)

    cliques = nx.find_cliques(g)
    good_ones = set()
    for cliq in cliques:
        if len(cliq) >= 3 and set(cliq).intersection(t_nodes):
            for c in itertools.combinations(cliq, 3):
                fs = frozenset(c)
                if fs.intersection(t_nodes):
                    good_ones.add(fs)

    return len(good_ones)


def q2():
    with open('input.txt', 'r') as f:
        return ','.join([_ for _ in sorted(max(nx.find_cliques(nx.from_edgelist({tuple(line.split('-')) for line in f.read().splitlines()})), key=lambda cliq: len(cliq)))])


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
