---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: lib/data_structure/segment_tree.py
    title: lib/data_structure/segment_tree.py
  - icon: ':heavy_check_mark:'
    path: lib/sample/io.py
    title: lib/sample/io.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    from lib.sample.io import read\nfrom lib.data_structure.segment_tree import SegmentTree\n\
    \nMOD = 998244353\n\n\ndef op(fi, fj):\n    ai, bi = fi\n    aj, bj = fj\n   \
    \ return aj * ai % MOD, (aj * bi % MOD + bj) % MOD\n\n\ndef main():\n    n, q\
    \ = map(int, read().split())\n    ab = [tuple(map(int, read().split())) for _\
    \ in range(n)]\n    st = SegmentTree(n, op, (1, 0))\n    st.build(ab)\n    for\
    \ _ in range(q):\n        query = [int(i) for i in read().split()]\n        if\
    \ query[0] == 0:\n            p, c, d = query[1:]\n            st.set(p, (c, d))\n\
    \        else:\n            l, r, x = query[1:]\n            a, b = st.query(l,\
    \ r)\n            print((a * x % MOD + b) % MOD)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - lib/data_structure/segment_tree.py
  - lib/sample/io.py
  isVerificationFile: true
  path: verify/data_structure/point_set_range_composite.test.py
  requiredBy: []
  timestamp: '2022-07-30 19:51:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/point_set_range_composite.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/point_set_range_composite.test.py
- /verify/verify/data_structure/point_set_range_composite.test.py.html
title: verify/data_structure/point_set_range_composite.test.py
---
