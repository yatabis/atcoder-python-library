---
title: FenwickTree
documentation_of: //lib/data_structure/fenwick_tree.py
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
def build(self, a: Sequence)
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
