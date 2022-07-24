---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/predecessor_problem
    links:
    - https://judge.yosupo.jp/problem/predecessor_problem
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    from lib.sample.io import read\nfrom lib.data_structure.treap import Treap\n\n\
    \ndef main():\n    n, q = map(int, read().split())\n    t = read()\n    treap\
    \ = Treap()\n    for i, ti in enumerate(t):\n        if ti == \"1\":\n       \
    \     treap.insert(i)\n    for _ in range(q):\n        i, k = map(int, read().split())\n\
    \        if i == 0:\n            if not treap.contains(k):\n                treap.insert(k)\n\
    \        elif i == 1:\n            if treap.contains(k):\n                treap.delete(k)\n\
    \        elif i == 2:\n            print(int(treap.contains(k)))\n        elif\
    \ i == 3:\n            x = treap.ge(k)\n            print(x if x is not None else\
    \ -1)\n        elif i == 4:\n            x = treap.le(k)\n            print(x\
    \ if x is not None else -1)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: verify/data_structure/predecessor_problem.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: verify/data_structure/predecessor_problem.test.py
layout: document
redirect_from:
- /verify/verify/data_structure/predecessor_problem.test.py
- /verify/verify/data_structure/predecessor_problem.test.py.html
title: verify/data_structure/predecessor_problem.test.py
---
