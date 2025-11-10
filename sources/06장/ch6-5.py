"""프로그램 6.5: 원형 큐 방식으로 구현한 ArrayQueue 클래스"""

class ArrayQueue:
    """원형 큐 방식으로 구현한 큐 클래스"""

    def __init__(self, SIZE = 100):	# 공백 큐를 생성한다.
        self._data = [None] * SIZE	# 큐 원소 저장을 위한 리스트
        self._size = 0			# 큐 원소의 개수 저장
        self._front = 0			# 리스트에서 front 원소의 위치 저장

    def empty(self):		# 큐가 공백이면 True, 아니면 False를 반환한다.
        return self._size == 0

    def enqueue(self, item):	# 큐에 원소 item을 삽입한다.
        if self._size == len(self._data): # 큐 오버플로우 발생
            return None
        rear = (self._front + self._size) % len(self._data)
        self._data[rear] = item
        self._size += 1

    def dequeue(self):		# 큐의 front 원소를 삭제한 후 반환한다.
        if self.empty():
            return None
        item = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item

    def first(self):		# 큐의 front 원소를 반환한다.
        if self.empty():
            return None
        return self._data[self._front]

 
def num_interval(L, K):
    """리스트 L에서 부분합이 K인 구간의 개수를 반환한다."""
    Q = ArrayQueue()			        # 공백 큐 생성
    count = 0			        # 부분합이 K인 구간의 개수 기록
    sub_sum = 0                         # 큐에 저장된 숫자들의 합

    for x in L:
        Q.enqueue(x)		        # 큐에 그다음 숫자 삽입
        sub_sum += x 			# 부분합 갱신
        if sub_sum == K:                # 부분합이 K인 구간 찾음
            count += 1	                # 구간 개수 증가
        elif sub_sum > K:               # 부분합이 K 초과하면
            while sub_sum > K:		# 부분합이 K 이하가 될 때까지 삭제
                sub_sum -= Q.dequeue()	# 큐에서 원소 삭제와 부분합 갱신
            if sub_sum == K:            # 부분합이 K인 구간 찾음
                count += 1		# 구간 개수 증가
    return count	                # 부분합이 K인 구간 개수 반환


# main
L = [3, 1, 4, 2, 1, 3, 1, 6]
K = 7
print(num_interval(L, K))
