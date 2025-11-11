"""프로그램 10.11: UFSet 클래스"""

class UFSet:
    """분리된 집합 모임을 위한 union-find 클래스"""
    
    def __init__(self, n):
        self.parent = [-1]*n	# 집합 모임 ({0}, {1}, ... , {n-1}) 생성

    def union(self, i, j):	# i와 j를 대표 원소로 하는 집합의 합집합
        temp = self.parent[i] + self.parent[j]	# 노드 수의 합
        if self.parent[i] > self.parent[j]:	# 트리 j의 노드가 많음
            self.parent[i] = j			# j가 i의 부모가 됨
            self.parent[j] = temp
        else:					# 트리 i의 노드가 많음
            self.parent[j] = i 			# i가 j의 부모가 됨
            self.parent[i] = temp

    def find(self, i):		# i가 포함된 집합의 대표 원소 반환
        root = i
        while self.parent[root] >= 0:	    # 루트 탐색
            root = self.parent[root]
        while i != root:		    # i의 조상을 root의 자식으로 둠
            self.parent[i], i = root, self.parent[i]
        return root

    def root(self, i):		# i가 대표 원소이면 True, 아니면 False 반환
        return self.parent[i] < 0
