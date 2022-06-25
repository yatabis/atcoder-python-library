# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb
import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    t = int(read())
    for _ in range(t):
        a, b = map(int, read().split())
        print(a + b)


if __name__ == '__main__':
    main()
