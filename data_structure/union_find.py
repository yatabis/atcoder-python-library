class UnionFind:
    def __init__(self, n):
        self._n = n
        self._parents = [-1] * n

    def find(self, x):
        if self._parents[x] < 0:
            return x
        else:
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)
