"""프로그램 9.3: 레벨 순위 순회"""
from collections import deque

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크

def visit(data):
    """노드 방문 시 수행할 작업을 정의한다."""
    print(data, end='')

def levelorder(root):
    """큐를 이용하여 레벨 순서로 트리를 순회한다."""
    Q = deque()			    # 공백 큐 생성 (collections.deque 사용)
    if root is None: 	            # 루트가 널 노드이면 작업 종료
        return
    Q.append(root)		    # 루트를 큐에 삽입
    while len(Q) > 0:		    # 큐가 공백이 아니면 반복
        node = Q.popleft()	    # 큐에서 front 노드를 꺼냄
        visit(node.data)	    # 노드 방문 (자료 원소에 대한 작업)
        if node.left is not None:   # 왼쪽 자식이 존재하면 큐에 삽입
            Q.append(node.left)
        if node.right is not None:  # 오른쪽 자식이 존재하면 큐에 삽입
            Q.append(node.right) 

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

print('levelorder seq : ', end='')
levelorder(root)
print()

