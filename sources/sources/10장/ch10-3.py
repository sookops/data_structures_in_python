"""프로그램 10.3: 이진 탐색 트리에서 삽입을 수행하는 프로그램"""

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
    node = root		            # 루트 노드부터 탐색
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
	
# 이진 탐색 트리 테스트
D = [35, 10, 50, 5, 20, 40, 70, 15, 45]
root = None

for x in D:                         # 삽입 연산으로 이진 탐색 트리 구축
    root = insert(root, x)

ret = search(root, 50)
if ret:
    print("success")
else:
    print("fail")

ret = search(root, 65)
if ret:
    print("success")
else:
    print("fail")    
