# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from lib.sample.io import read
from lib.data_structure.segment_tree import SegmentTree


def main():
    n, q = map(int, read().split())
    a = [int(i) for i in read().split()]
    st = SegmentTree(n, lambda x, y: x + y, 0)
    st.build(a)
    for _ in range(q):
        l, r = map(int, read().split())
        print(st.query(l, r))


if __name__ == '__main__':
    main()