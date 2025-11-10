"""요셉 문제를 해결하는 프로그램의 수행 시간 비교"""

import time
from collections import deque

def josephus(n, k):
    """n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로
    살아남을 수 있는 위치를 반환한다."""
    Q = deque()				# deque를 이용하여 공백 큐 생성
    for i in range(1, n+1):		# 1부터 n까지 큐에 삽입
        Q.append(i)
    while len(Q) > 1:			# 마지막 한 명이 남을 때까지 반복
        for _ in range(k-1):		# k-1번째 사람까지는 큐에 다시 삽입
            Q.append(Q.popleft())
        Q.popleft()			# k번째 사람 제거
    return Q[0]				# 최후의 생존자 위치

def josephus_up(n, k):
    """n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로
    살아남을 수 있는 위치를 반환한다."""
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

def josephus_opt1(n, k):
    """n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로
    살아남을 수 있는 위치를 반환한다."""
    Q = deque()				# deque를 이용하여 공백 큐 생성
    for i in range(1, n+1):		# 1부터 n까지 큐에 삽입
        Q.append(i)
    q_size = n				# 현재 큐의 크기
    while q_size > 1:			# 마지막 한 명이 남을 때까지 반복
        Q.rotate(-(k-1))

        Q.popleft()			# k번째 위치 제거
        q_size -= 1			# 큐 크기 갱신
    return Q[0]				# 최후의 생존자 위치

def josephus_opt2(n, k):
    """n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로
    살아남을 수 있는 위치를 반환한다."""
    Q = deque()				# deque를 이용하여 공백 큐 생성
    for i in range(1, n+1):		# 1부터 n까지 큐에 삽입
        Q.append(i)
    q_size = n				# 현재 큐의 크기
    while q_size > 1:			# 마지막 한 명이 남을 때까지 반복
        Q.rotate(-((k-1) % q_size))

        Q.popleft()			# k번째 위치 제거
        q_size -= 1			# 큐 크기 갱신
    return Q[0]				# 최후의 생존자 위치

def josephus_opt3(n, k):        # 재귀 관계를 이용한 해법
    stack = []                          # 공백 스택 생성

    for i in range(n, 0, -1):
        stack.append((i, k))

    result = 0   
    while len(stack) > 0:
        n, k = stack.pop()
        if n == 1:
            result = 1
        else:
            result = (result + k-1) % n + 1

    return result

# main program
n, k = map(int, input().split())

s = time.time()
res5 = josephus_opt3(n, k)
t = time.time()
print(res5, "time =", t-s)

s = time.time()
res4 = josephus_opt2(n, k)
t = time.time()
print(res4, "time =", t-s)

s = time.time()
res3 = josephus_opt1(n, k)
t = time.time()
print(res3, "time =", t-s)

s = time.time()
res2 = josephus(n, k)
t = time.time()
print(res2, "time =", t-s)

s = time.time()
res1 = josephus_up(n, k)
t = time.time()
print(res1, "time =", t-s)







