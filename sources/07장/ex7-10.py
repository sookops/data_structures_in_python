"""연습문제 7.13: 연결리스트의 모든 원소를 출력하는 프로그램"""

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
    return p		    # 시작 노드의 링크를 반환한다.

def print_all_recursive(p):
    """재귀 함수로 연결리스트 모든 원소를 출력한다."""
    if p is None: return            # 종료 조건 
    print(p.data, end=' ')          # 데이터 필드에 저장된 원소 출력
    print_all_recursive(p.next)     # p의 다음 노드를 가지고 재귀 호출

def print_reverse_recursive(p):
    """재귀 함수로 연결리스트 모든 원소를 역순으로 출력한다."""
    if p is None: return            # 종료 조건 
    print_reverse_recursive(p.next) # p의 다음 노드를 가지고 재귀 호출
    print(p.data, end=' ')          # 데이터 필드에 저장된 원소 출력
    
# main program
L = [100, 200, 400, 500]
head = create_linkedlist(L)

print_all_recursive(head)
print()
print_reverse_recursive(head)
print()

