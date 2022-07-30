# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
from lib.sample.io import read
from lib.data_structure.segment_tree import SegmentTree


def main():
    n, q = map(int, read().split())
    a = [int(i) for i in read().split()]
    st = SegmentTree(n, lambda x, y: x + y, 0)
    st.build(a)
    for _ in range(q):
        query = [int(i) for i in read().split()]
        if query[0] == 0:
            st.add(query[1], query[2])
        else:
            print(st.query(query[1], query[2]))


if __name__ == '__main__':
    main()
