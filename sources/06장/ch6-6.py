"""프로그램 6.6: collection.deque를 사용하여 구현한 Queue 클래스"""

from collections import deque

class Queue:
    '''collections.deque를 사용하여 구현한 큐 클래스'''
    def __init__(self):			# 공백 큐를 생성한다.
        self._data = deque()		

    def empty(self):		        # 큐가 공백이면 True, 아니면 False를 반환한다.
        return len(self._data) == 0		

    def enqueue(self, item):	        # 큐에 원소 item을 삽입한다.
        self._data.append(item)

    def dequeue(self):			# 큐의 front 원소를 삭제한 후 반환한다.
        if self.empty(): return None
        return self._data.popleft()

    def first(self):			# 큐의 front 원소를 반환한다.
        if self.empty(): return None
        return self._data[0]

 
