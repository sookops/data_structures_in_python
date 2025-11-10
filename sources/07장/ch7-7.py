"""프로그램 7.7: 연결리스트를 사용하여 구현한 Stack 클래스"""

class Stack:
    """연결리스트를 사용하여 구현한 스택 클래스"""

    class _Node:			    # 노드 클래스 (내부 클래스로 정의)
        def __init__(self, item=None, link=None):
            self._data = item
            self._next = link

    def __init__(self):			    # 공백 스택 생성
        self._head = self._Node()	    # 헤더 노드 생성

    def empty(self):			    # 공백이면 True, 아니면 False 반환
        return self._head._next is None

    def push(self, item):		    # 스택에 원소 item 삽입
        self._head._next = self._Node(item, self._head._next)

    def pop(self):			    # 스택의 top 원소를 삭제한 후 반환
        if self.empty():
            return None
        item = self._head._next._data
        self._head._next = self._head._next._next
        return item

    def peek(self):			    # 스택의 top 원소 반환
        if self.empty():
            return None
        return self._head._next._data

# main program
S = Stack()
for x in range(1, 10):
    S.push(x)

while not S.empty():
    print(S.peek(), end=' ')
    S.pop()
print()
