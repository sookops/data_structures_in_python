"""프로그램 7.1: 연결리스트 노드를 위한 클래스"""

class Node:
    def __init__(self, item=None, link=None):
        self.data = item    # 자료 원소 저장
        self.next = link    # 링크 저장
