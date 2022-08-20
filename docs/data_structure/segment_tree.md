---
title: SegmentTree
documentation_of: //lib/data_structure/segment_tree.py
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
