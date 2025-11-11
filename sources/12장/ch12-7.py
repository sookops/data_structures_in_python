"""프로그램 12.7: 인접 리스트 기반의 다익스트라 알고리즘의 구현"""

import heapq 								

def dijkstra_heap(G, src):
    """최단 경로를 구하는 다익스트라 알고리즘의 구현:
    인접 리스트 G로 표현된 가중치 그래프에서 출발점이 src인 최단 거리 리스트와
    최단 경로 트리를 반환한다. G[v] = [(인접 정점, 가중치), ...]"""
    n = len(G)					# 정점 수
    parent = [src] * n				# 부모 포인터 배열 초기화
    parent[src] = -1				# src를 루트로 설정
    dist = [float('inf')]*n			# 최단 거리 배열 dist 초기화
    dist[src] = 0				# src의 최단 거리

    H = [(0, src)]				# 힙에 출발점 삽입 (거리, 정점)
    while len(H) > 0:				# 공백 힙이 될 때까지 반복
        length, v = heapq.heappop(H)		# (거리, 정점) 쌍
        if length > dist[v]: 		        # v의 최단 거리가 이미 구해진 경우
            continue				# 무시함
        for w, c in G[v]:			# v의 인접 정점 w와 가중치 c
            length = dist[v] + c		# 정점 v를 지나는 경로의 길이
            if length < dist[w]:		# 더 짧은 경로 발견
                dist[w] = length		# 최단 거리 변경
                heapq.heappush(H, (length, w))	# 힙에 삽입
                parent[w] = v			# w의 부모를 v로 설정

    return dist, parent			        # 최단 거리와 최단 경로 트리 반환			    # 최소 신장 트리의 에지 리스트 반환

	
def create_weighted_adj_list():     # 방향 그래프의 가중치 인접 리스트를 구축하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    G = [[] for _ in range(n)]	                # 인접 리스트의 초기화
    for _ in range(m):		                # m개 에지 입력
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        G[v].append((w, c))		        # v에 대한 리스트에 (w, c) 추가
    return G				        # 가중치 인접 리스트 반환

# main program
G = create_weighted_adj_list()

dist, parent = dijkstra_heap(G, 0)
print('최단 거리 :', dist)
print('최단 경로 트리 :', parent) 

# 그래프 예
'''
6
12
0 1 35
0 4 20
0 5 40
1 2 20
1 4 40
2 1 10
3 1 10
3 2 10
3 4 15
4 3 20
4 5 10
5 4 10
'''
    
