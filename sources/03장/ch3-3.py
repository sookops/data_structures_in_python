"""프로그램 3.3: 파이썬 리스트의 깊은 복사"""

import copy

L = [[0]*5 for _ in range(4)]
M = copy.deepcopy(L)

L[0][0] = 1
print(M[0][0])
