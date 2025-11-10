"""프로그램 10.2: 이진 탐색 트리에서 탐색을 수행하는 프로그램"""

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

# 이진 탐색 트리 테스트
D = [35, 10, 50, 5, 20, 40, 70, 15, 45]
root = None

nodes = []
for x in D:
    nodes.append(BinNode(x))
    
root = nodes[0]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[4].left = nodes[7]
nodes[5].right = nodes[8]

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
