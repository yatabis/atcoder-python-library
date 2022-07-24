# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem
from lib.sample.io import read
from lib.data_structure.treap import Treap


def main():
    n, q = map(int, read().split())
    t = read()
    treap = Treap()
    for i, ti in enumerate(t):
        if ti == "1":
            treap.insert(i)
    for _ in range(q):
        i, k = map(int, read().split())
        if i == 0:
            if not treap.contains(k):
                treap.insert(k)
        elif i == 1:
            if treap.contains(k):
                treap.delete(k)
        elif i == 2:
            print(int(treap.contains(k)))
        elif i == 3:
            x = treap.ge(k)
            print(x if x is not None else -1)
        elif i == 4:
            x = treap.le(k)
            print(x if x is not None else -1)


if __name__ == '__main__':
    main()
