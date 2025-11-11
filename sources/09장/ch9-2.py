"""프로그램 9.2: 전위 순회, 중위 순회, 후위 순회 프로그램"""

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크

def visit(data):
    """노드 방문 시 수행할 작업을 정의한다."""
    print(data, end='')

def preorder(node):
    """전위 순회 (vLR)"""
    if node is None: return     # 널 노드이면 퇴각함
    visit(node.data)		# 노드 방문(자료 원소에 대한 작업)
    preorder(node.left)		# 왼쪽 부트리를 순회
    preorder(node.right)	# 오른쪽 부트리를 순회

def inorder(node):
    """중위 순회 (LvR)"""
    if node is None: return	# 널 노드이면 퇴각함
    inorder(node.left)		# 왼쪽 부트리를 순회
    visit(node.data)		# 노드 방문(자료 원소에 대한 작업)
    inorder(node.right)		# 오른쪽 부트리를 순회

def postorder(node):
    """후위 순회 (LRv)"""
    if node is None: return	# 널 노드이면 퇴각함
    postorder(node.left)	# 왼쪽 부트리를 순회
    postorder(node.right)	# 오른쪽 부트리를 순회
    visit(node.data)		# 노드 방문(자료 원소에 대한 작업)

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

print('preorder seq : \t', end='')
preorder(root)
print()

print('inorder seq : \t', end='')
inorder(root)
print()

print('postorder seq : ', end='')
postorder(root)
print()

