# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from lib.sample.io import read


def main():
    n, q = map(int, read().split())
    a = [int(i) for i in read().split()]
    aa = [0] * (n + 1)
    for i in range(n):
        aa[i + 1] = aa[i] + a[i]
    for _ in range(q):
        l, r = map(int, read().split())
        print(aa[r] - aa[l])


if __name__ == '__main__':
    main()
