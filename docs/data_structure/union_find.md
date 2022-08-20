---
title: UnionFind
documentation_of: //lib/data_structure/union_find.py
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
> $O(N)$

---

```python
def union(self, x: int, y: int) -> bool
```

> x と y をマージする<br>
> マージに成功した場合 `True` 、失敗した場合 `False` を返す<br>
> amortized $O(\alpha(N))$

---

```python
def find(self, x: int) -> int
```

> x を含む連結成分の根を返す<br>
> amortized $O(\alpha(N))$

---

```python
def same(self, x: int, y: int) -> bool
```

> x と y が同じ連結成分に含まれているかを返す<br>
> amortized $O(\alpha(N))$

---
