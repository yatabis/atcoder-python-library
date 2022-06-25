---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: sample/io.py
    title: sample/io.py
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
    from sample.io import read\n\n\ndef main():\n    q = int(read())\n    a = {}\n\
    \    for _ in range(q):\n        query = read().split()\n        if query[0] ==\
    \ \"0\":\n            k, v = query[1:]\n            a[k] = v\n        else:\n\
    \            k = query[1]\n            print(a.get(k, \"0\"))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - sample/io.py
  isVerificationFile: true
  path: data_structure/associative_array.test.py
  requiredBy: []
  timestamp: '2022-06-25 16:50:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: data_structure/associative_array.test.py
layout: document
redirect_from:
- /verify/data_structure/associative_array.test.py
- /verify/data_structure/associative_array.test.py.html
title: data_structure/associative_array.test.py
---
