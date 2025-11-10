"""프로그램 7.8: 연결리스트를 사용하여 구현한 Queue 클래스"""

class Queue:
    """연결리스트를 사용하여 구현한 큐 클래스"""
    class _Node:	                    # 노드 클래스 (내부 클래스)
        def __init__(self, item=None, link=None):
            self._data = item
            self._next = link

    def __init__(self):	                    # 공백 큐를 생성한다.
        self._head = self._Node()	    # 헤더 노드 생성
        self._tail = self._head

    def empty(self):	                    # 공백이면 True, 아니면 False 반환
        return self._head._next is None

    def enqueue(self, item):	            # 큐에 원소 item 삽입
        new_node = self._Node(item)	    # 새 노드 생성
        self._tail._next = new_node	    # 끝 노드로 설정
        self._tail = new_node

    def dequeue(self):	                    # 큐의 front 원소를 삭제한 후 반환
        if self.empty():
            return None
        item = self._head._next._data       # 반환할 원소
        self._head._next = self._head._next._next
        if self._head._next is None: 	    # # 헤더 노드만 남으면
            self._tail = self._head	    # tail도 헤더 노드를 가리킴
        return item

    def first(self):	                    # 큐의 front 원소 반환
        if self.empty():
            return None
        return self._head._next._data

# main program
Q = Queue()
for x in range(1, 10):
    Q.enqueue(x)

while not Q.empty():
    print(Q.first(), end=' ')
    Q.dequeue()
print()
