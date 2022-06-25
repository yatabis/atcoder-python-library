---
data:
  _extendedDependsOn: []
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
    import sys\n\n\ndef read():\n    return sys.stdin.readline().rstrip()\n\n\ndef\
    \ main():\n    t = int(read())\n    for _ in range(t):\n        a, b = map(int,\
    \ read().split())\n        print(a + b)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: sample/many_aplusb.test.py
  requiredBy: []
  timestamp: '2022-06-25 15:55:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: sample/many_aplusb.test.py
layout: document
redirect_from:
- /verify/sample/many_aplusb.test.py
- /verify/sample/many_aplusb.test.py.html
title: sample/many_aplusb.test.py
---
