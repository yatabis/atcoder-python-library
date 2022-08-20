---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/point_add_range_sum__segment_tree.test.py
    title: verify/data_structure/point_add_range_sum__segment_tree.test.py
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/point_set_range_composite.test.py
    title: verify/data_structure/point_set_range_composite.test.py
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/static_range_sum__segment_tree.test.py
    title: verify/data_structure/static_range_sum__segment_tree.test.py
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/staticrmq.test.py
    title: verify/data_structure/staticrmq.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "T = \"Monoid\"\n\n\nclass SegmentTree:\n    def __init__(self, n: int, op,\
    \ e):\n        self._n = n\n        self._op = op\n        self._e = e\n     \
    \   self._a = [self._e] * (n * 2)\n\n    def build(self, a):\n        for i, ai\
    \ in enumerate(a, self._n):\n            self._a[i] = ai\n        for i in range(self._n\
    \ - 1, 0, -1):\n            self._a[i] = self._op(self._a[2 * i], self._a[2 *\
    \ i + 1])\n\n    def set(self, i: int, x: T):\n        i += self._n\n        self._a[i]\
    \ = x\n        while i > 1:\n            i //= 2\n            self._a[i] = self._op(self._a[2\
    \ * i], self._a[2 * i + 1])\n\n    def query(self, l: int, r: int) -> T:\n   \
    \     l += self._n\n        r += self._n\n        vl, vr = self._e, self._e\n\
    \        while l < r:\n            if l % 2:\n                vl = self._op(vl,\
    \ self._a[l])\n                l += 1\n            if r % 2:\n               \
    \ vr = self._op(self._a[r - 1], vr)\n            l //= 2\n            r //= 2\n\
    \        return self._op(vl, vr)\n\n    def at(self, i: int) -> T:\n        return\
    \ self._a[i + self._n]\n"
  dependsOn: []
  isVerificationFile: false
  path: lib/data_structure/segment_tree.py
  requiredBy: []
  timestamp: '2022-08-20 14:37:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify/data_structure/staticrmq.test.py
  - verify/data_structure/point_add_range_sum__segment_tree.test.py
  - verify/data_structure/static_range_sum__segment_tree.test.py
  - verify/data_structure/point_set_range_composite.test.py
documentation_of: lib/data_structure/segment_tree.py
layout: document
title: SegmentTree
---

## SegmentTree

モノイド $T$ の要素数 $N$ の配列に対して、要素の一点変更と任意区間のモノイド積の取得をともに $O(\log N)$ で行うことができるデータ構造。

## Implementations

```python
def __init__(self, n: int, op: Callable[[T, T], T], e: T)
```

> サイズ `n` の SegmentTree を単位元で初期化する<br>
> `op` : モノイド積を計算する関数<br>
> `e` : モノイドの単位元<br>
> $O(N)$

---

```python
def build(self, a: Sequence[T])
```

> `a` で初期化する<br>
> `a` のサイズが SgementTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(N)$

---

```python
def set(self, i: int, x: T)
```

> `i` 番目の要素を `x` に更新する<br>
> `i` が SegmentTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---

```python
def query(self, l: int, r: int) -> T
```

> 区間 `[l, r)` の和を返す<br>
> `l >= r` のときは単位元を返す<br>
> `l` または `r` が SegmentTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---

```python
def at(self, i: int) -> T
```

> `i` 番目の要素の値を返す<br>
> `i` が SegmentTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---
