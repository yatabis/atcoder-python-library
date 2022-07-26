---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: lib/data_structure/union_find.py
    title: UnionFind
  - icon: ':heavy_check_mark:'
    path: lib/sample/io.py
    title: lib/sample/io.py
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
    from lib.sample.io import read\nfrom lib.data_structure.union_find import UnionFind\n\
    \n\ndef main():\n    n, q = map(int, read().split())\n    uf = UnionFind(n)\n\
    \    for _ in range(q):\n        t, u, v = map(int, read().split())\n        if\
    \ t == 0:\n            uf.union(u, v)\n        else:\n            print(int(uf.same(u,\
    \ v)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - lib/sample/io.py
  - lib/data_structure/union_find.py
  isVerificationFile: true
  path: verify/data_structure/union_find.test.py
  requiredBy: []
  timestamp: '2022-06-26 23:15:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/union_find.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/union_find.test.py
- /verify/verify/data_structure/union_find.test.py.html
title: verify/data_structure/union_find.test.py
---
