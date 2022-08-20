---
data:
  _extendedDependsOn:
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    from lib.sample.io import read\n\n\ndef main():\n    n, q = map(int, read().split())\n\
    \    a = [int(i) for i in read().split()]\n    aa = [0] * (n + 1)\n    for i in\
    \ range(n):\n        aa[i + 1] = aa[i] + a[i]\n    for _ in range(q):\n      \
    \  l, r = map(int, read().split())\n        print(aa[r] - aa[l])\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - lib/sample/io.py
  isVerificationFile: true
  path: verify/data_structure/static_range_sum.test.py
  requiredBy: []
  timestamp: '2022-07-27 01:28:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/static_range_sum.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/static_range_sum.test.py
- /verify/verify/data_structure/static_range_sum.test.py.html
title: verify/data_structure/static_range_sum.test.py
---
