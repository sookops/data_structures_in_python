"""프로그램 9.5: 이진 트리를 복사하는 프로그램"""

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

def copy_tree(node):
    """이진 트리를 복사하는 재귀 함수"""
    if node is None:            	# 널 노드이면 None 반환
        return None
    clon = BinNode(node.data)		# 노드 생성 및 데이터 복사
    clon.left = copy_tree(node.left)	# 왼쪽 부트리 복사
    clon.right = copy_tree(node.right)	# 오른쪽 부트리 복사
    return clon										# 복사된 루트 노드의 링크 반환

def create_sample_tree():       # 이진 트리 생성
    E = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    tree = []
    for item in E:
        tree.append(BinNode(item))

    tree[0].left = tree[1]
    tree[0].right = tree[2]
    tree[1].left = tree[3]
    tree[1].right = tree[4]
    tree[2].left = tree[5]
    tree[2].right = tree[6]
    tree[4].left = tree[7]
    tree[5].right = tree[8]
    return tree[0]              # 루트 반환

# main program
root = create_sample_tree()
clon_root = copy_tree(root)
print('size =', size(clon_root))
print('height =', height(clon_root))
