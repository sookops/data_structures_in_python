"""프로그램 8.8: bisect 모듈의 사용 예"""

from bisect import *

L = [5, 12, 18, 25, 25, 25, 30, 30, 32, 38]

print(bisect_left(L, 12))	# 1
print(bisect_left(L, 19))	# 3
print(bisect_left(L, 25))	# 3
print(bisect_left(L, 40))	# 10

print(bisect_right(L, 12))	# 2
print(bisect_right(L, 19))	# 3
print(bisect_right(L, 25))	# 6
print(bisect_right(L, 40))	# 10

insort_left(L, 19)
insort_right(L, 31)
print(L)		# [5, 12, 18, 19, 25, 25, 25, 30, 30, 31, 32, 38]
