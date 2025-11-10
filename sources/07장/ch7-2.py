"""프로그램 7.2: 그림 7.2의 연결리스트를 생성하는 프로그램"""

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
   
# main program
L = [100, 200, 400, 500]
head = create_linkedlist(L)

print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next)


L = []
head = create_linkedlist(L)
print(head)
