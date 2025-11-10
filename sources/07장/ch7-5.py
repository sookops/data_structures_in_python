"""프로그램 7.5: 연결리스트에서 삽입을 수행하는 프로그램"""

class Node:
    def __init__(self, item=None, link=None):
        self.data = item    # 자료 원소 저장
        self.next = link    # 링크 저장

def create_linkedlist(L):
    """리스트 L의 요소들로 연결리스트를 생성하여 반환한다."""
    q = None		    # 다음 노드의 링크, 초깃값은 None
    L.reverse()
    for x in L:
        p = Node(x, q)	    # p는 항목이 x이고 링크가 q인 노드를 참조한다.
        q = p		    # q는 새로 생성된 노드를 참조한다.
    return q		    # 시작 노드의 링크를 반환한다.

def print_all(head):
    """연결리스트 head의 모든 원소를 출력한다."""
    p = head
    while p is not None:	    # p가 널 링크를 가질 때까지 반복함
        print(p.data, end=' ')	    # 데이터 필드에 저장된 원소 출력
        p = p.next		    # p에 다음 노드의 링크를 배정함
    print()
    
def find(head, k):
    """연결리스트 head에서 k-번째 원소를 반환한다. (k >= 0)"""
    if k < 0: return None	    # k가 음수면 None을 반환함
    p = head
    for i in range(k):		    # 링크를 k번 따라감
        if p is None: 		    # 노드가 존재하지 않으면 None을 반환함
            return None
        p = p.next		    # p에 다음 노드의 링크를 배정함
    if p is None: 	            # k-번째 노드가 없으면 None을 반환함
        return None
    return p.data		    # k-번째 원소 반환함

def index(head, value):
    """연결리스트 head에서 value의 최초 위치인 첨자를 반환한다."""
    i = 0                           # 첨자를 저장함
    p = head
    while p is not None:	    # p가 널 링크를 가질 때까지 반복함
        if p.data == value: 	    # value를 발견하면 원소의 첨자를 반환함
            return i
        p = p.next		    # p에 다음 노드의 링크를 배정함
        i += 1			    # 첨자 1 증가
    return None			    # 존재하지 않으면 None을 반환함

def add_front(head, new_node):
    """연결리스트 head의 맨 앞에 노드 new_node를 삽입한다."""
    new_node.next = head	    # head를 new_node의 다음 노드로 설정
    return new_node		    # 새로운 시작 노드의 링크를 반환함

def add_node(prev, new_node):
    """노드 prev의 뒤에 노드 new_node를 삽입한다."""
    new_node.next = prev.next	    # prev의 다음 노드를 new의 다음 노드로 설정
    prev.next = new_node	    # new_node를 prev의 다음 노드로 설정
	
# main program
L = [100, 200, 400, 500]
head = create_linkedlist(L)

head = add_front(head, Node(50))
add_node(head.next.next, Node(300))
print_all(head)

