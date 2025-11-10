"""프로그램 7.14: 이중 연결리스트를 사용하여 구현한 Deuque 클래스"""

class Deque:
    """헤더 노드를 가진 원형 이중 연결리스트를 사용하여 구현한 데크 클래스"""
    
    class _DNode:                       # 노드 클래스 (내부 클래스)
        def __init__(self, item=None, next_link=None, prev_link=None):
            self._data = item		# 자료 원소 저장
            self._next = next_link	# 다음 노드의 링크 저장
            self._prev = prev_link	# 이전 노드의 링크 저장

    def __init__(self):			# 공백 데크를 생성한다.
        self._head = self._DNode(0)     # 헤더 노드에 데크 크기를 저장함
        self._head._next = self._head._prev = self._head

    def empty(self):			# 공백이면 True, 아니면 False 반환
        return self._head._data == 0

    def __len__(self):			# 데크 크기 반환
        return self._head._data

    def add_first(self, item):	        # 데크의 맨 앞에 원소 item 삽입
        new_node  = self._DNode(item, self._head._next, self._head)
        self._head._next._prev = new_node
        self._head._next = new_node
        self._head._data += 1

    def add_last(self, item):	        # 데크의 맨 끝에 원소 item 삽입
        new_node = self._DNode(item, self._head, self._head._prev)
        self._head._prev._next = new_node
        self._head._prev = new_node
        self._head._data += 1

    def _delete_node(self, p):		# 노드 p를 삭제 (클래스 내부에서만 사용)
        if p is self._head:
            raise ValueError("헤더 노드를 삭제할 수 없습니다.")
        p._prev._next = p._next
        p._next._prev = p._prev
        self._head._data -= 1
        return p._data

    def pop_first(self):		# 데크의 맨 앞 원소를 삭제한 후 반환
        if self.empty():        	# 공백이면 None 반환
            return None
        return self._delete_node(self._head._next)  # 삭제된 원소 반환

    def pop_last(self):			# 데크의 맨 끝 원소를 삭제한 후 반환
        if self.empty(): 		# 공백이면 None 반환
            return None
        return self._delete_node(self._head._prev)  # 삭제된 원소 반환

    def first(self):			# 데크의 맨 앞 원소 반환
        if self.empty(): 		# 공백이면 None 반환
            return None
        return self._head._next._data

    def last(self):                     # 데크의 맨 끝 원소 반환
        if self.empty():
            return None
        return self._head._prev._data
		
# main program
D = Deque()
for i in range(1, 4):
    D.add_first(2*i)
    D.add_last(2*i+1)

print('데크의 크기:', len(D))
print(D.first(), D.last())
print(D.pop_first(), D.pop_last())
while not D.empty():
    print(D.pop_first(), end = ' ')
print()

