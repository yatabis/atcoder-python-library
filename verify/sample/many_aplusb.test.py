# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb
from lib.sample.io import read


def main():
    t = int(read())
    for _ in range(t):
        a, b = map(int, read().split())
        print(a + b)


if __name__ == '__main__':
    main()
