"""프로그램 10.4: 이진 탐색 트리에서 삭제를 수행하는 프로그램"""

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크

def visit(data):
    """노드 방문 시 수행할 작업을 정의한다."""
    print(data, end=' ')

def inorder(node):
    """중위 순회 (LvR)"""
    if node is None: return	# 널 노드이면 퇴각함
    inorder(node.left)		# 왼쪽 부트리를 순회
    visit(node.data)		# 노드 방문(자료 원소에 대한 작업)
    inorder(node.right)		# 오른쪽 부트리를 순회
    
def search(root, item):
    """이진 탐색 트리에서 item을 가진 노드의 링크를 반환한다."""
    node = root.left		    # 원래 트리의 루트
    while node is not None: 	    # 널 링크가 아니면 반복
        if item == node.data: 	    # 탐색 성공
            return node
        if item < node.data: 	    # 왼쪽 부트리 탐색
            node = node.left
        else:	    		    # 오른쪽 부트리 탐색
            node = node.right
    return None			    # 탐색 실패

def insert(root, item):
    """이진 탐색 트리에 item을 가진 노드를 삽입하고, 루트 노드를 반환한다."""
    if root is None:		    # 공백이면, 새 노드를 루트로 반환
        return BinNode(item)
    
    parent = None		    # 초기에 None을 부모로 설정
    node = root		            # 초기에 루트를 자식으로 설정
    while node is not None:	    # 널 링크를 만날 때까지 반복
        parent = node		    # 자식 레벨로 내려옴
        if item < node.data:	    # item이 작으면 왼쪽 부트리 탐색
            node = node.left
        else:			    # item이 크면 오른쪽 부트리 탐색
            node = node.right
       
    new_node = BinNode(item)	    # 삽입할 새 노드 생성
    if item < parent.data:
        parent.left = new_node	    # 왼쪽 자식으로 삽입
    else:
        parent.right = new_node	    # 오른쪽 자식으로 삽입

    return root			    # 루트 노드의 링크 반환

def delete(root, item):
    """이진 탐색 트리에 item을 가진 노드를 삭제하고, 루트 노드를 반환한다."""

    # ① item을 가진 노드 X를 탐색함
    parent = None			        # 초기에 None을 부모로 설정
    X = root				        # 초기에 루트를 자식으로 설정
    while X is not None and item != X.data:     # 삭제할 노드 X 탐색
        parent = X				# 자식 레벨로 내려옴
        if item < X.data: X = X.left 	        # 왼쪽 부트리 탐색
        else: X = X.right	                # 오른쪽 부트리 탐색

    if X is None: 			        # 삭제할 노드가 없으면 작업 종료
        return root

    # ② 자식이 둘 다 있으면 중위 후속자 Y를 탐색함
    if X.left is not None and X.right is not None:
        parent = X
        Y = X.right
        while Y.left is not None:		# 중위 후속자 탐색
            parent = Y			        # 자식 레벨로 내려옴
            Y = Y.left			        # 왼쪽 자식 배정

        X.data = Y.data			        # 중위 후속자 Y의 원소를 X로 옮김
        X = Y					# X가 실제 삭제할 노드를 가리키게 함

    # ③ 노드 X 제거 – 부모와 자식을 찾아 연결함(자식이 있으면)
    son = X.right if X.left is None else X.left	    # 노드 X의 자식 배정
    if parent is None: 				# 부모가 없으면 son이 루트가 됨
        root = son
    else:					# son을 parent의 자식으로 설정
        if X.data < parent.data: parent.left = son
        else: parent.right = son

    return root				        # 루트 노드의 링크 반환
	
# 이진 탐색 트리 테스트
D = [35, 10, 50, 5, 20, 40, 70, 15, 45]
root = None

for x in D:             # 삽입 연산으로 이진 탐색 트리 구축
    root = insert(root, x)

inorder(root)
print()

root = delete(root, 5)
inorder(root)
print()

root = delete(root, 20)
inorder(root)
print()

root = delete(root, 35)
inorder(root)
print()
