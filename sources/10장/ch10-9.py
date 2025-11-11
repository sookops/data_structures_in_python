"""프로그램 10.9: heapq 모듈을 이용한 힙 정렬"""

from heapq import *

def heapsort(S):
    """heapq 모듈을 이용한 힙 정렬로 리스트 S를 정렬한다."""
    heapify(S)					# 힙 초기화
    S[:] = [heappop(S) for _ in range(len(S))]	# 정렬 작업

# 테스트
L = [20, 35, 25, 40, 15, 10, 30]
heapsort(L)
print(*L)
