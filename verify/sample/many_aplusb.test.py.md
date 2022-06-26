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
    PROBLEM: https://judge.yosupo.jp/problem/many_aplusb
    links:
    - https://judge.yosupo.jp/problem/many_aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb\n\
    from lib.sample.io import read\n\n\ndef main():\n    t = int(read())\n    for\
    \ _ in range(t):\n        a, b = map(int, read().split())\n        print(a + b)\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - lib/sample/io.py
  isVerificationFile: true
  path: verify/sample/many_aplusb.test.py
  requiredBy: []
  timestamp: '2022-06-26 23:15:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/sample/many_aplusb.test.py
layout: document
redirect_from:
- /verify/verify/sample/many_aplusb.test.py
- /verify/verify/sample/many_aplusb.test.py.html
title: verify/sample/many_aplusb.test.py
---
