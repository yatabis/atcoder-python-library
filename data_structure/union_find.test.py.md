---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/union_find.py
    title: data_structure/union_find.py
  - icon: ':heavy_check_mark:'
    path: sample/io.py
    title: sample/io.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    from sample.io import read\nfrom data_structure.union_find import UnionFind\n\n\
    \ndef main():\n    n, q = map(int, read().split())\n    uf = UnionFind(n)\n  \
    \  for _ in range(q):\n        t, u, v = map(int, read().split())\n        if\
    \ t == 0:\n            uf.union(u, v)\n        else:\n            print(int(uf.same(u,\
    \ v)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - sample/io.py
  - data_structure/union_find.py
  isVerificationFile: true
  path: data_structure/union_find.test.py
  requiredBy: []
  timestamp: '2022-06-25 16:56:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: data_structure/union_find.test.py
layout: document
redirect_from:
- /verify/data_structure/union_find.test.py
- /verify/data_structure/union_find.test.py.html
title: data_structure/union_find.test.py
---
