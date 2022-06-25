---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: data_structure/union_find.test.py
    title: data_structure/union_find.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n):\n        self._n = n\n     \
    \   self._parents = [-1] * n\n\n    def find(self, x):\n        if self._parents[x]\
    \ < 0:\n            return x\n        else:\n            self._parents[x] = self.find(self._parents[x])\n\
    \            return self._parents[x]\n\n    def union(self, x, y):\n        x\
    \ = self.find(x)\n        y = self.find(y)\n\n        if x == y:\n           \
    \ return\n\n        if self._parents[x] > self._parents[y]:\n            x, y\
    \ = y, x\n\n        self._parents[x] += self._parents[y]\n        self._parents[y]\
    \ = x\n\n    def same(self, x, y):\n        return self.find(x) == self.find(y)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/union_find.py
  requiredBy: []
  timestamp: '2022-06-25 16:56:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - data_structure/union_find.test.py
documentation_of: data_structure/union_find.py
layout: document
redirect_from:
- /library/data_structure/union_find.py
- /library/data_structure/union_find.py.html
title: data_structure/union_find.py
---
