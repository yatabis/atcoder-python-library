---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import random\nfrom typing import Optional\n\n\nclass TreapNode:\n\
    \    def __init__(self, value):\n        self.value = value\n        self.priority\
    \ = random()\n        self.left: Optional[TreapNode] = None\n        self.right:\
    \ Optional[TreapNode] = None\n        self.parent: Optional[TreapNode] = None\n\
    \n    def rotate_left(self):\n        pivot = self.right\n        self.right =\
    \ pivot.left\n        if pivot.left is not None:\n            pivot.left.parent\
    \ = self\n        pivot.left = self\n        pivot.parent = self.parent\n    \
    \    self.parent = pivot\n        if pivot.parent is not None:\n            parent\
    \ = pivot.parent\n            if parent.left is self:\n                parent.left\
    \ = pivot\n            elif parent.right is self:\n                parent.right\
    \ = pivot\n\n    def rotate_right(self):\n        pivot = self.left\n        self.left\
    \ = pivot.right\n        if pivot.right is not None:\n            pivot.right.parent\
    \ = self\n        pivot.right = self\n        pivot.parent = self.parent\n   \
    \     self.parent = pivot\n        if pivot.parent is not None:\n            parent\
    \ = pivot.parent\n            if parent.left is self:\n                parent.left\
    \ = pivot\n            elif parent.right is self:\n                parent.right\
    \ = pivot\n\n    def tree(self):\n        nodes = []\n        if self.left is\
    \ not None:\n            nodes += self.left.tree()\n        nodes.append(str(self))\n\
    \        if self.right is not None:\n            nodes += self.right.tree()\n\
    \        return nodes\n\n    def __str__(self):\n        return f\"{self.value}({self.priority}\
    \ p{self.parent.value if self.parent else ''})\"\n\n\nclass Treap:\n    def __init__(self):\n\
    \        self.root: Optional[TreapNode] = None\n\n    def _rotate_left(self, node:\
    \ TreapNode):\n        if node is self.root:\n            self.root = node.right\n\
    \        node.rotate_left()\n\n    def _rotate_right(self, node: TreapNode):\n\
    \        if node is self.root:\n            self.root = node.left\n        node.rotate_right()\n\
    \n    def contains(self, x) -> bool:\n        node = self.root\n        while\
    \ node is not None:\n            if x == node.value:\n                return True\n\
    \            if x < node.value:\n                node = node.left\n          \
    \  else:\n                node = node.right\n        return False\n\n    def insert(self,\
    \ x):\n        new_node = TreapNode(x)\n\n        if self.root is None:\n    \
    \        self.root = new_node\n            return\n\n        node = self.root\n\
    \        while True:\n            if x < node.value:\n                if node.left\
    \ is None:\n                    new_node.parent = node\n                    node.left\
    \ = new_node\n                    break\n                node = node.left\n  \
    \          else:\n                if node.right is None:\n                   \
    \ new_node.parent = node\n                    node.right = new_node\n        \
    \            break\n                node = node.right\n\n        while new_node.parent\
    \ is not None and new_node.priority > new_node.parent.priority:\n            if\
    \ new_node is new_node.parent.left:\n                self._rotate_right(new_node.parent)\n\
    \            elif new_node is new_node.parent.right:\n                self._rotate_left(new_node.parent)\n\
    \            else:\n                raise ValueError\n\n    def delete(self, x):\n\
    \        if self.root is None:\n            raise KeyError('delete(): Treap is\
    \ empty')\n\n        node = self.root\n        while node.value != x:\n      \
    \      if x < node.value:\n                if node.left is None:\n           \
    \         raise KeyError(x)\n                node = node.left\n            else:\n\
    \                if node.right is None:\n                    raise KeyError(x)\n\
    \                node = node.right\n\n        while node.left is not None or node.right\
    \ is not None:\n            if node.left is None:\n                self._rotate_left(node)\n\
    \            else:\n                self._rotate_right(node)\n\n        if node\
    \ is node.parent.left:\n            node.parent.left = None\n        elif node\
    \ is node.parent.right:\n            node.parent.right = None\n        else:\n\
    \            raise ValueError\n\n    def lt(self, x) -> Optional:\n        if\
    \ self.root is None:\n            return None\n\n        node = self.root\n  \
    \      lt = None\n        while node is not None:\n            value = node.value\n\
    \            if value < x:\n                if lt is None or value > lt:\n   \
    \                 lt = value\n                node = node.right\n            else:\n\
    \                node = node.left\n        return lt\n\n    def le(self, x) ->\
    \ Optional:\n        if self.root is None:\n            return None\n\n      \
    \  node = self.root\n        le = None\n        while node is not None:\n    \
    \        value = node.value\n            if value <= x:\n                if le\
    \ is None or value > le:\n                    le = value\n                node\
    \ = node.right\n            else:\n                node = node.left\n        return\
    \ le\n\n    def gt(self, x) -> Optional:\n        if self.root is None:\n    \
    \        return None\n\n        node = self.root\n        gt = None\n        while\
    \ node is not None:\n            value = node.value\n            if value > x:\n\
    \                if gt is None or value < gt:\n                    gt = value\n\
    \                node = node.left\n            else:\n                node = node.right\n\
    \        return gt\n\n    def ge(self, x) -> Optional:\n        if self.root is\
    \ None:\n            return None\n\n        node = self.root\n        ge = None\n\
    \        while node is not None:\n            value = node.value\n           \
    \ if value >= x:\n                if ge is None or value < ge:\n             \
    \       ge = value\n                node = node.left\n            else:\n    \
    \            node = node.right\n        return ge\n\n    def __str__(self):\n\
    \        return f\"Treap<{', '.join(self.root.tree())}>\"\n"
  dependsOn: []
  isVerificationFile: false
  path: lib/data_structure/treap.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: lib/data_structure/treap.py
layout: document
redirect_from:
- /library/lib/data_structure/treap.py
- /library/lib/data_structure/treap.py.html
title: lib/data_structure/treap.py
---
