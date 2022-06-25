# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array
from sample.io import read


def main():
    q = int(read())
    a = {}
    for _ in range(q):
        query = read().split()
        if query[0] == "0":
            k, v = query[1:]
            a[k] = v
        else:
            k = query[1]
            print(a.get(k, "0"))


if __name__ == '__main__':
    main()
