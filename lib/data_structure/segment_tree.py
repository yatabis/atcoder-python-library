T = int


class SegmentTree:
    def __init__(self, n: int, op, e):
        self._n = n
        self._op = op
        self._e = e
        self._a = [self._e] * (n * 2)

    def build(self, a):
        for i, ai in enumerate(a, self._n):
            self._a[i] = ai
        for i in range(self._n - 1, 0, -1):
            self._a[i] = self._op(self._a[2 * i], self._a[2 * i + 1])

    def add(self, i: int, x: T):
        i += self._n
        self._a[i] += x
        while i > 1:
            i //= 2
            self._a[i] = self._op(self._a[2 * i], self._a[2 * i + 1])

    def set(self, i: int, x: T):
        i += self._n
        self._a[i] = x
        while i > 1:
            i //= 2
            self._a[i] = self._op(self._a[2 * i], self._a[2 * i + 1])

    def query(self, l: int, r: int) -> T:
        l += self._n
        r += self._n
        vl, vr = self._e, self._e
        while l < r:
            if l % 2:
                vl = self._op(vl, self._a[l])
                l += 1
            if r % 2:
                vr = self._op(self._a[r - 1], vr)
            l //= 2
            r //= 2
        return self._op(vl, vr)

    def at(self, i: int) -> T:
        return self._a[i + self._n]
