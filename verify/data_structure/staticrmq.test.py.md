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
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    from lib.sample.io import read\nfrom lib.data_structure.segment_tree import SegmentTree\n\
    \n\ndef main():\n    n, q = map(int, read().split())\n    a = [int(i) for i in\
    \ read().split()]\n    st = SegmentTree(n, min, 10**10)\n    st.build(a)\n   \
    \ for _ in range(q):\n        l, r = map(int, read().split())\n        print(st.query(l,\
    \ r))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - lib/sample/io.py
  - lib/data_structure/segment_tree.py
  isVerificationFile: true
  path: verify/data_structure/staticrmq.test.py
  requiredBy: []
  timestamp: '2022-07-30 18:22:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/staticrmq.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/staticrmq.test.py
- /verify/verify/data_structure/staticrmq.test.py.html
title: verify/data_structure/staticrmq.test.py
---
