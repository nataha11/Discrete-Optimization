#!/usr/bin/python3

from collections import namedtuple
import numpy as np
from scipy.optimize import linprog

row = namedtuple('row', 'ind weight covered_c')

def find_value(rows, not_colrs, cover):

    value = 0
    covered = set()

    for row in rows:
        if not cover[row.ind]:
            continue
        for c in row.covered_c:
            covered.add(c)
        value += row.weight

    bol = (len(covered) == not_colrs)
    return (bol, value)

def solver(rows, not_colrs):

    not_col_r = len(rows)
    weights = np.array([r.weight for r in rows])
    inc = np.zeros((not_col_r, not_colrs), 'int')

    for r in rows:
        for c in r.covered_c:
            inc[r.ind][c] = 1

    solution = linprog(weights, A_ub=-inc.T, b_ub=-np.ones((not_colrs, 1)), bounds=(0, None))
    best_cover = None
    best_value = None

    for _ in range(100_000):
        cover = np.random.rand(not_col_r) > solution.x
        is_cover, value = find_value(rows, not_colrs, cover)
        if is_cover:
            if best_value is None or best_value > value:
                best_cover = cover
                best_value = value

    if best_value is None:
        return
    res = np.arange(1, not_col_r + 1)[best_cover]
    print(' '.join(map(str, res)))

def main():
    
    # Parse the input
    not_colrs, not_col_r = map(int, input().split())
    rows = []

    for i in range(not_col_r):
        row_weight, *covered_column = input().split()
        rows.append(row(i, int(row_weight), np.array(covered_column, 'int')))

    # Solve
    solver(rows, not_colrs)

if __name__ == '__main__':
    main()