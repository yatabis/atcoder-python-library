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
  code: "from typing import List\n\nT = int\n\n\nclass FenwickTree:\n    def __init__(self,\
    \ n: int):\n        self._n = n\n        self._a = [0] * (n + 1)\n\n    def build(self,\
    \ a: List[T]):\n        for i, ai in enumerate(a):\n            self.add(i, ai)\n\
    \n    def add(self, i: int, x: T):\n        i += 1\n        while i <= self._n:\n\
    \            self._a[i] += x\n            i += i & -i\n\n    def set(self, i:\
    \ int, x: T):\n        self.add(i, x - self._sum(i) + self._sum(i - 1))\n\n  \
    \  def sum(self, l: int, r: int) -> T:\n        return self._sum(r) - self._sum(l\
    \ - 1)\n\n    def _sum(self, i: int) -> T:\n        i += 1\n        s = 0\n  \
    \      while i > 0:\n            s += self._a[i]\n            i -= i & -i\n  \
    \      return s\n\n    def at(self, i: int) -> T:\n        return self._sum(i)\
    \ - self._sum(i - 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: lib/data_structure/fenwick_tree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: lib/data_structure/fenwick_tree.py
layout: document
redirect_from:
- /library/lib/data_structure/fenwick_tree.py
- /library/lib/data_structure/fenwick_tree.py.html
title: lib/data_structure/fenwick_tree.py
---
