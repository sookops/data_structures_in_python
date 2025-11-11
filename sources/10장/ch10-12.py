"""프로그램 10.12: 친구 그룹 수를 구하는 프로그램"""

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

def groups(n, S):
    """n명의 친구 리스트 S에 대한 친구 그룹 수를 반환한다."""
    C = UFSet(n)		# n개의 원소를 가진 UFSet 객체 생성
    count = 0
    for p in S:			# 합집합을 구하는 과정
        C.union(C.find(p[0]), C.find(p[1]))
    for i in range(n):
        if C.root(i):           #그룹의 수 계산
            count += 1
    return count

# 테스트
n = 10
S = [(0, 3), (1, 4), (2, 5), (3, 8), (4, 6), (5, 6), (7, 9)]
print(groups(n, S))
