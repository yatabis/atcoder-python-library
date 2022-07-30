# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from lib.sample.io import read
from lib.data_structure.fenwick_tree import FenwickTree


def main():
    n, q = map(int, read().split())
    a = [int(i) for i in read().split()]
    ft = FenwickTree(n)
    ft.build(a)
    for _ in range(q):
        l, r = map(int, read().split())
        print(ft.sum(l, r - 1))


if __name__ == '__main__':
    main()