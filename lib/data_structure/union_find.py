class UnionFind:
    def __init__(self, n: int):
        self._n = n
        self._parents = [-1] * n

    def find(self, x: int) -> int:
        if self._parents[x] < 0:
            return x
        else:
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
