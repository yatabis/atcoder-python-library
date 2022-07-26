from typing import List

T = int


class FenwickTree:
    def __init__(self, n: int):
        self._n = n
        self._a = [0] * (n + 1)

    def build(self, a: List[T]):
        for i, ai in enumerate(a):
            self.add(i, ai)

    def add(self, i: int, x: T):
        i += 1
        while i <= self._n:
            self._a[i] += x
            i += i & -i

    def set(self, i: int, x: T):
        self.add(i, x - self._sum(i) + self._sum(i - 1))

    def sum(self, l: int, r: int) -> T:
        return self._sum(r) - self._sum(l - 1)

    def _sum(self, i: int) -> T:
        i += 1
        s = 0
        while i > 0:
            s += self._a[i]
            i -= i & -i
        return s

    def at(self, i: int) -> T:
        return self._sum(i) - self._sum(i - 1)
