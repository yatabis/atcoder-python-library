---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: lib/data_structure/fenwick_tree.py
    title: FenwickTree
  - icon: ':heavy_check_mark:'
    path: lib/sample/io.py
    title: lib/sample/io.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    from lib.sample.io import read\nfrom lib.data_structure.fenwick_tree import FenwickTree\n\
    \n\ndef main():\n    n, q = map(int, read().split())\n    a = [int(i) for i in\
    \ read().split()]\n    ft = FenwickTree(n)\n    ft.build(a)\n    for _ in range(q):\n\
    \        l, r = map(int, read().split())\n        print(ft.sum(l, r - 1))\n\n\n\
    if __name__ == '__main__':\n    main()"
  dependsOn:
  - lib/sample/io.py
  - lib/data_structure/fenwick_tree.py
  isVerificationFile: true
  path: verify/data_structure/static_range_sum_fenwick_tree.test.py
  requiredBy: []
  timestamp: '2022-07-28 01:03:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/static_range_sum_fenwick_tree.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/static_range_sum_fenwick_tree.test.py
- /verify/verify/data_structure/static_range_sum_fenwick_tree.test.py.html
title: verify/data_structure/static_range_sum_fenwick_tree.test.py
---