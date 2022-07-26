---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    from lib.sample.io import read\nfrom lib.data_structure.fenwick_tree import FenwickTree\n\
    \n\ndef main():\n    n, q = map(int, read().split())\n    a = [int(i) for i in\
    \ read().split()]\n    ft = FenwickTree(n)\n    ft.build(a)\n    for _ in range(q):\n\
    \        query = [int(i) for i in read().split()]\n        if query[0] == 0:\n\
    \            ft.add(query[1], query[2])\n        else:\n            print(ft.sum(query[1],\
    \ query[2] - 1))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: verify/data_structure/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/point_add_range_sum.test.py
- /verify/verify/data_structure/point_add_range_sum.test.py.html
title: verify/data_structure/point_add_range_sum.test.py
---
