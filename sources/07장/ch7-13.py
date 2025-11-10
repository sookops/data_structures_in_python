"""프로그램 7.13: 원형 이중 연결리스트에서 노드를 삭제하는 프로그램"""

class DNode:
    def __init__(self, item=None, next_link=None, prev_link=None):
        self.data = item		# 자료 원소 저장
        self.next = next_link		# 다음 노드의 링크 저장
        self.prev = prev_link		# 이전 노드의 링크 저장

def create_doublylinkedlist(L):
    """리스트 L의 요소들로 헤더 노드를 가진 원형 이중 연결리스트를 생성하여 반환한다."""
    head = DNode()			# 헤더 노드 생성
    head.next = head.prev = head	# 헤더 노드 하나만 있는 구조
    for x in L:	
        p = DNode(x, head, head.prev) 	# 끝 노드로 삽입될 새 노드 생성
        head.prev.next = p	 	# 이전 끝 노드가 새 노드를 가리킴
        head.prev = p			# 헤더 노드가 새 노드를 가리킴
    return head		    		# 헤더 노드 반환

def delete(p):			        # 노드 p를 삭제
    if p is not None or p is not head:	# 헤더 노드는 삭제되지 않음
        p.prev.next = p.next            # p의 이전 노드가 p의 다음 노드를 가리킴
        p.next.prev = p.prev            # p의 다음 노드가 p의 이전 노드를 가리킴
		
# main program
L = [100, 200, 400, 500]
head = create_doublylinkedlist(L)

delete(head.next.next)
delete(head.prev)

p = head.next
while p is not head:
    print(p.data, end=' ')
    p = p.next
print()

