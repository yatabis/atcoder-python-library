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
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    from lib.sample.io import read\n\n\ndef main():\n    q = int(read())\n    a =\
    \ {}\n    for _ in range(q):\n        query = read().split()\n        if query[0]\
    \ == \"0\":\n            k, v = query[1:]\n            a[k] = v\n        else:\n\
    \            k = query[1]\n            print(a.get(k, \"0\"))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - lib/sample/io.py
  isVerificationFile: true
  path: verify/data_structure/associative_array.test.py
  requiredBy: []
  timestamp: '2022-06-26 23:15:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/data_structure/associative_array.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/associative_array.test.py
- /verify/verify/data_structure/associative_array.test.py.html
title: verify/data_structure/associative_array.test.py
---
