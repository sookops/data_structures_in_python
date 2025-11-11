"""프로그램 9.1: 이진 트리의 노드 클래스"""

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크
