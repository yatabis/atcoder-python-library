# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
from lib.sample.io import read
from lib.data_structure.union_find import UnionFind


def main():
    n, q = map(int, read().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, u, v = map(int, read().split())
        if t == 0:
            uf.union(u, v)
        else:
            print(int(uf.same(u, v)))


if __name__ == '__main__':
    main()
