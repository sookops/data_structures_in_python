"""프로그램 12.5: 인접 리스트 기반의 크루스칼 알고리즘의 구현"""

import heapq				

class UFSet:
    def __init__(self, n):
        self.parent = [-1]*n		# 집합 모임 ({0}, {1}, ... , {n-1}) 생성

    def union(self, i, j):		# i와 j를 대표 원소로 하는 집합의 합집합 구성
        temp = self.parent[i] + self.parent[j]	    # 노드 수의 합
        if self.parent[i] > self.parent[j]:	    # 트리 j의 노드가 많음
            self.parent[i] = j			    # j가 i의 부모가 됨
            self.parent[j] = temp
        else:					    # 트리 i의 노드가 많음
            self.parent[j] = i 			    # i가 j의 부모가 됨
            self.parent[i] = temp

    def find(self, i):			# i가 포함된 집합의 대표 원소 반환
        root = i
        while self.parent[root] >= 0:	# 루트 탐색
            root = self.parent[root]
            while i != root:		# i의 조상을 root의 자식으로 둠
                self.parent[i], i = root, self.parent[i]
        return root

    def root(self, i):			# i가 대표 원소이면 True, 아니면 False 반환
        return self.parent[i] < 0

	    
def kruskal(G):
    """크루스칼 알고리즘의 구현:
    인접 리스트 G로 표현된 가중치 그래프의 최소 신장 트리를 구해 에지 리스트를 
    반환한다. G[v] = [(인접 정점, 가중치), ...]"""
    n = len(G)		                # 정점 수
    mst = []			        # 최소 신장 트리의 에지 리스트
    C = UFSet(n)			# n개의 원소를 가진 UFSet 객체 생성
    H = []                              # 최소 힙으로 사용할 리스트
    for v in range(n):			# H에 모든 에지를 삽입
        for w, c in G[v]:		# v의 인접 정점 w와 가중치 c
            if v < w: 		        # 중복 방지를 위한 조건
                H.append((c, v, w))     # 가중치 기준으로 힙에 삽입
    heapq.heapify(H)			# H를 힙으로 초기화
    
    while len(mst) < n-1:	            # n-1개의 에지를 선택할 때까지 반복
        if len(H) == 0:         	    # 힙이 공백이면 None을 반환
            return None
        c, v, w = heapq.heappop(H)	    # 힙 H에서 에지 삭제       
        if C.find(v) != C.find(w):	    # 양 끝점이 다른 집합에 속하면
            mst.append((v, w, c))           # (v, w, c)를 트리 에지로 추가
            C.union(C.find(v), C.find(w))   # 합집합 수행

    return mst			            # 최소 신장 트리의 에지 리스트 반환

	
def create_weighted_adj_list():     # 무향 그래프의 가중치 인접 리스트를 구축하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    G = [[] for _ in range(n)]	                # 인접 리스트의 초기화
    for _ in range(m):		                # m개 에지 입력
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        G[v].append((w, c))		        # v에 대한 리스트에 (w, c) 추가
        G[w].append((v, c))		        # w에 대한 리스트에 (v, c) 추가
    return G				        # 가중치 인접 리스트 반환

# main program
G = create_weighted_adj_list()

A = kruskal(G)
if A == None: print("Not exist")
else:
    print('최소 신장 트리 :', [x[:2] for x in A])
    print('총 비용 =', sum([x[2] for x in A])) 

# 그래프 예
'''
8
11
0 3 10
0 2 45
0 4 40
1 2 25
1 4 15
1 5 35
2 4 30
2 7 50
3 7 20
5 6 55
5 7 60
'''

