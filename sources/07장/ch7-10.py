"""프로그램 7.10: 이중 연결리스트 노드를 위한 클래스"""

class DNode:
    def __init__(self, item=None, next_link=None, prev_link=None):
        self.data = item		# 자료 원소 저장
        self.next = next_link		# 다음 노드의 링크 저장
        self.prev = prev_link		# 이전 노드의 링크 저장

