"""프로그램 4.8: 최대 재귀 깊이를 변경하는 프로그램의 예"""

import sys
print(sys.getrecursionlimit())	# 현재 최대 재귀 깊이를 출력함
sys.setrecursionlimit(10000)	# 최대 재귀 깊이를 10000으로 변경함

