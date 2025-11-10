"""프로그램 10.1: 이진 탐색 트리의 노드 클래스"""

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
    
# 이진 탐색 트리의 구축 테스트
D = [35, 10, 50, 5, 20, 40, 70, 15, 45]
head = BinNode(float('inf'))    # 헤더 노드

nodes = []
for x in D:
    nodes.append(BinNode(x))
head.left = nodes[0]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[4].left = nodes[7]
nodes[5].right = nodes[8]

inorder(head.left)
