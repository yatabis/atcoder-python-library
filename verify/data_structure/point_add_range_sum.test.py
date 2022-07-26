# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
from lib.sample.io import read
from lib.data_structure.fenwick_tree import FenwickTree


def main():
    n, q = map(int, read().split())
    a = [int(i) for i in read().split()]
    ft = FenwickTree(n)
    ft.build(a)
    for _ in range(q):
        query = [int(i) for i in read().split()]
        if query[0] == 0:
            ft.add(query[1], query[2])
        else:
            print(ft.sum(query[1], query[2] - 1))


if __name__ == '__main__':
    main()
