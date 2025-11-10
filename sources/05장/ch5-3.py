"""프로그램 5.3: 파이썬 리스트를 사용하여 구현한 Stack 클래스"""

class Stack:
    """파이썬 리스트를 사용하여 구현한 스택 클래스"""
    def __init__(self):		# 공백 스택을 생성한다.
        self._data = []

    def empty(self):	        # 스택이 공백이면 True, 아니면 False를 반환한다.
        return len(self._data) == 0

    def push(self, item):	# 스택에 원소 item을 삽입한다.
        self._data.append(item)

    def pop(self):		# 스택의 top 원소를 삭제한 후 반환한다.
        if self.empty():
            return None
        return self._data.pop()

    def peek(self):		# 스택의 top 원소를 반환한다.
        if self.empty():
            return None
        return self._data[-1]
