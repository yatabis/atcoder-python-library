# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite
from lib.sample.io import read
from lib.data_structure.segment_tree import SegmentTree

MOD = 998244353


def op(fi, fj):
    ai, bi = fi
    aj, bj = fj
    return aj * ai % MOD, (aj * bi % MOD + bj) % MOD


def main():
    n, q = map(int, read().split())
    ab = [tuple(map(int, read().split())) for _ in range(n)]
    st = SegmentTree(n, op, (1, 0))
    st.build(ab)
    for _ in range(q):
        query = [int(i) for i in read().split()]
        if query[0] == 0:
            p, c, d = query[1:]
            st.set(p, (c, d))
        else:
            l, r, x = query[1:]
            a, b = st.query(l, r)
            print((a * x % MOD + b) % MOD)


if __name__ == '__main__':
    main()
