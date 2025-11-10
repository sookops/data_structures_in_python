"""프로그램 9.6: 전위 순서와 중위 순서로 정의되는 이진 트리를 구축하는 재귀 함수"""

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크

def visit(data):
    """노드 방문 시 수행할 작업을 정의한다."""
    print(data, end='')

def size(node):
    """이진 트리의 노드 수를 구하는 재귀 함수"""
    if node is None: 	            # 널 노드이면 0 반환
        return 0
    return 1 + size(node.left) + size(node.right)

def height(node):
    """이진 트리의 높이를 구하는 재귀 함수"""
    if node is None: 	             # 널 노드이면 -1 반환
        return -1
    return 1 + max(height(node.left), height(node.right))

def make_binarytree(A, B):
    """전위 순서 A, 중위 순서 B로 정의되는 이진 트리를 구축하는 재귀 함수"""
    if len(A) == 0:     	# 공백 리스트이면 NOne을 반환
        return None
    root = BinNode(A[0])	# 노드 생성 및 루트 노드의 데이터 복사
    k = B.index(A[0])		# 중위 순서에서 루트 원소의 위치 탐색
    root.left = make_binarytree(A[1:k+1], B[:k])	 # 왼쪽 부트리 생성
    root.right = make_binarytree(A[k+1:], B[k+1:])	 # 오른쪽 부트리 생성
    return root			# 루트 노드의 링크 반환

# main program
A = 'ABDEHCFIG'
B = 'DBHEAFICG'
root = make_binarytree(A, B)
print('size =', size(root))
print('height =', height(root))
