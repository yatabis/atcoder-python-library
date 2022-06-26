---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/union_find.test.py
    title: verify/data_structure/union_find.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n: int):\n        self._n = n\n\
    \        self._parents = [-1] * n\n\n    def find(self, x: int) -> int:\n    \
    \    if self._parents[x] < 0:\n            return x\n        else:\n         \
    \   self._parents[x] = self.find(self._parents[x])\n            return self._parents[x]\n\
    \n    def union(self, x: int, y: int) -> bool:\n        x = self.find(x)\n   \
    \     y = self.find(y)\n\n        if x == y:\n            return False\n\n   \
    \     if self._parents[x] > self._parents[y]:\n            x, y = y, x\n\n   \
    \     self._parents[x] += self._parents[y]\n        self._parents[y] = x\n   \
    \     return True\n\n    def same(self, x: int, y: int) -> bool:\n        return\
    \ self.find(x) == self.find(y)\n"
  dependsOn: []
  isVerificationFile: false
  path: lib/data_structure/union_find.py
  requiredBy: []
  timestamp: '2022-06-26 23:15:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify/data_structure/union_find.test.py
documentation_of: lib/data_structure/union_find.py
layout: document
title: UnionFind
---

## Union-Find Tree (Disjoint Set Union)

データの集合を素集合に分割してもつデータ構造

以下の二つの操作をともに $O(\alpha(N))$ で行える（$\alpha(N)$ はアッカーマン関数 $A(N, N)$ の逆関数）

- union: 2つの集合をマージする
- find: ある要素がどの集合に含まれるかを求める

## Implementations

```python
def __init__(self, n: int)
```

> サイズ $n$ の UnionFind を生成する<br>
> $O(1)$

---

```python
def union(self, x: int, y: int) -> bool
```

> x と y をマージする<br>
> マージに成功した場合 `True` 、失敗した場合 `False` を返す<br>
> $O(\alpha(N))$

---

```python
def find(self, x: int) -> int
```

> x を含む連結成分の根を返す<br>
> $O(\alpha(N))$

---

```python
def same(self, x: int, y: int) -> bool
```

> x と y が同じ連結成分に含まれているかを返す<br>
> $O(\alpha(N))$

---
