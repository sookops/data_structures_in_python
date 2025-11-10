"""프로그램 10.10: heapq 모듈에서 비교 기준을 변경하는 예"""

from heapq import *

# 최대 힙 구성
L = [3, 6, 2, 1, 7, 4]
H = [(-x, x) for x in L]	# L의 요소 x를 튜플 (-x, x)로 변환
heapify(H)			# 힙 초기화
while len(H) > 0:		# 힙 H가 공백이 될 때까지 반복
    print(heappop(H)[1])	# 7, 6, 4, 3, 2, 1 순으로 출력

# 문자열의 길이를 기준으로 최소 힙 구성
L = ["apple", "banana", "cherry", "kiwi"]
H = [(len(x), x) for x in L]	# L의 요소 x를 튜플 (len(x), x)로 변환
heapify(H)			# 힙 초기화
while len(H) > 0:		# 힙 H가 공백이 될 때까지 반복
    print(heappop(H)[1])        # kiwi, apple, banana, cherry 순으로 출력
