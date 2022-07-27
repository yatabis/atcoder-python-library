---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/point_add_range_sum.test.py
    title: verify/data_structure/point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: verify/data_structure/static_range_sum_fenwick_tree.test.py
    title: verify/data_structure/static_range_sum_fenwick_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "T = int\n\n\nclass FenwickTree:\n    def __init__(self, n: int):\n      \
    \  self._n = n\n        self._a = [0] * (n + 1)\n\n    def build(self, a):\n \
    \       for i, ai in enumerate(a):\n            self.add(i, ai)\n\n    def add(self,\
    \ i: int, x: T):\n        i += 1\n        while i <= self._n:\n            self._a[i]\
    \ += x\n            i += i & -i\n\n    def set(self, i: int, x: T):\n        self.add(i,\
    \ x - self._sum(i) + self._sum(i - 1))\n\n    def sum(self, l: int, r: int) ->\
    \ T:\n        return self._sum(r) - self._sum(l - 1)\n\n    def _sum(self, i:\
    \ int) -> T:\n        i += 1\n        s = 0\n        while i > 0:\n          \
    \  s += self._a[i]\n            i -= i & -i\n        return s\n\n    def at(self,\
    \ i: int) -> T:\n        return self._sum(i) - self._sum(i - 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: lib/data_structure/fenwick_tree.py
  requiredBy: []
  timestamp: '2022-07-28 01:03:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify/data_structure/point_add_range_sum.test.py
  - verify/data_structure/static_range_sum_fenwick_tree.test.py
documentation_of: lib/data_structure/fenwick_tree.py
layout: document
title: FenwickTree
---

## Fenwick Tree (Binary Indexed Tree)

$T$ 型の要素数 $n$ の配列に対して、値の一点加算と区間和の取得をともに $O(\log{N})$ で行えるデータ構造。

区間和が効率的に計算できる累積和では値の更新に $O(N)$ かかるところ、
Fenwick Tree では値の更新とそれによる変化を効率的に反映することができる。

Segment Tree と比較して実装がシンプルで定数倍が軽いが、区間和を計算するためには $T$ に逆元が存在する必要がある。

また、imos 法的に使えば 区間加算、一点取得 としても使うことができる。

## Implementations

```python
def __init__(self, n: int)
```

> サイズ `n` の FenwickTree を生成する<br>
> 初期値はすべて $0$<br>
> （デフォルトでは $T$ = `int` として扱われる）<br> 
> $O(N)$

---

```python
def build(self, a: Sequence[T])
```

> `a` で初期化する<br>
> はみ出た分は無視される<br>
> $O(N\log{N})$

---

```python
def add(self, i: int, x: T)
```

> `i` 番目の要素に `x` を加算する<br>
> `i` が FenwickTree のサイズより大きい場合は無視される<br>
> $O(\log{N})$

---

```python
def set(self, i: int, x: T)
```

> `i` 番目の要素を `x` に更新する<br>
> `i` が FenwickTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---

```python
def sum(self, l: int, r: int) -> int
```

> 区間 `[l, r]` の和を返す<br>
> `l` または `r` が FenwickTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---

```python
def at(self, i: int) -> T
```

> `i` 番目の要素の値を返す<br>
> `i` が FenwickTree のサイズより大きい場合は `IndexError` を送出する<br>
> $O(\log{N})$

---
