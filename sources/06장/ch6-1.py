"""프로그램 6.1: 무선조종 자동차 문제를 위한 프로그램"""

from collections import deque

class Queue:
    '''collections.deque를 사용하여 구현한 큐 클래스'''
    def __init__(self):		    # 공백 큐를 생성한다.
        self._data = deque()		

    def empty(self):		    # 큐가 공백이면 True, 아니면 False를 반환한다.
        return len(self._data) == 0		

    def enqueue(self, item):	    # 큐에 원소 item을 삽입한다.
        self._data.append(item)

    def dequeue(self):		    # 큐의 front 원소를 삭제한 후 반환한다.
        if self.empty(): return None
        return self._data.popleft()

    def first(self):		    # 큐의 front 원소를 반환한다.
        if self.empty(): return None
        return self._data[0]

def min_clicks(t, a, b):
    """목표 지점 t, 전진 거리 a, 후진 거리 b일 때, 출발점 0에서 목표 지점에
도달하면 최소 클릭 수, 아니면 -1을 반환한다."""
    Q = Queue()			        # 공백 큐 생성
    D = [0]*(t+1)	        	# 0으로 초기화된 리스트 생성
    Q.enqueue(0)		        # 큐에 초기 위치 삽입
    while not Q.empty():        	# Q가 공백이 아니면 반복
        p = Q.dequeue() 	        # Q에서 front 원소 삭제
        if p == t: 	        	# 목표 지점 도달
            return D[t]		# 최소 클릭수 반환
        if p+a <= t and D[p+a] == 0: 	# 전진 버튼 클릭
            Q.enqueue(p+a)
            D[p+a] = D[p]+1
        if p-b > 0 and D[p-b] == 0:	# 후진 버튼 클릭
            Q.enqueue(p-b)
            D[p-b] = D[p]+1
    return -1				# 목표 지점 도달 불가능

# main program
print(min_clicks(9, 5, 2))
print(min_clicks(51, 8, 2))
