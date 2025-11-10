"""프로그램 6.10: 큐 시뮬레이션 방식으로 요셉 문제를 해결하는 개선된 프로그램"""

from collections import deque

def josephus_up(n, k):
    """요셉 문제를 해결하는 프로그램:
    n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로 살아남을 수 있는 
    위치를 반환한다."""
    Q = deque()				# deque를 이용하여 공백 큐 생성
    for i in range(1, n+1):		# 1부터 n까지 큐에 삽입
        Q.append(i)
    q_size = n				# 현재 큐의 크기
    while q_size > 1:			# 마지막 한 명이 남을 때까지 반복
        for _ in range((k-1) % q_size):	# k-1번째 위치까지는 큐에 다시 삽입
            Q.append(Q.popleft())
        Q.popleft()			# k번째 위치 제거
        q_size -= 1			# 큐 크기 갱신
    return Q[0]				# 최후의 생존자 위치

# main program
n, k = map(int, input().split())
print(josephus_up(n, k))
