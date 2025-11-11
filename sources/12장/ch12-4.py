"""프로그램 12.4: 인접 리스트 기반의 프림 알고리즘의 구현"""

import heapq

def prim_heap(G):
    """프림 알고리즘의 구현:
    인접 리스트 G로 표현된 가중치 그래프의 최소 신장 트리를 구해 에지 리스트를 
    반환한다. G[v] = [(인접 정점, 가중치), ...]"""
    n = len(G)				# 정점 수
    mst = []			        # 최소 신장 트리의 에지 리스트
    H = []				# 최소 힙
    selected = [False] * n		# 트리 정점이면 True, 아니면 False
    selected[0] = True			# 시작 정점 0을 트리 정점으로 설정
    for w, c in G[0]:			# 각 인접 정점 w와 가중치 c에 대해
        heapq.heappush(H, (c, 0, w))	# 시작 정점 0에 부속된 에지 삽입

    while len(mst) < n-1:	        # n-1개의 트리 에지를 선택할 때까지 반복
        if len(H) == 0:         	# 힙이 공백이면 None을 반환
            return None
        c, v, w = heapq.heappop(H)	# 힙 H에서 에지 삭제
        if selected[w]:         	# w가 트리 정점이면 무시
            continue
        selected[w] = True		# w를 트리 정점으로 설정
        mst.append((v, w, c))	        # (v, w, c)를 트리 에지로 추가
        for u, c in G[w]:		# w의 각 인접 정점 u와 가중치 c에 대해
            if not selected[u]:		# 비트리 에지를 힙에 삽입
                heapq.heappush(H, (c, w, u))

    return mst	                        # 최소 신장 트리의 에지 리스트 반환
	
def create_weighted_adj_list():     # 무향 그래프의 가중치 인접 리스트를 구축하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    G = [[] for _ in range(n)]	                # 인접 리스트를 위한 2차원 리스트
    for _ in range(m):		                # m개 에지 입력
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        G[v].append((w, c))		        # v에 대한 리스트에 (w, c) 추가
        G[w].append((v, c))		        # w에 대한 리스트에 (v, c) 추가
    return G				        # 가중치 인접 리스트 반환

# main program
G = create_weighted_adj_list()

A = prim_heap(G)
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
    
