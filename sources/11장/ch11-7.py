"""프로그램 11.7: 최단 경로 트리를 찾는 프로그램"""
    
# G : 파이썬 리스트로 구현된 인접 리스트 (전역 변수)
# visited : 정점 방문 여부를 기록하는 리스트, False로 초기화됨 (전역 변수)
# parent : 최단 경로 트리를 저장하는 리스트, -1로 초기화됨 (전역 변수)

from collections import deque

def shortest_path(v):
    queue = deque()			# 공백 큐 생성 (collections.deque 사용)
    visited[v] = True			# 정점 v를 방문한 것으로 기록
    queue.append(v)			# 시작 정점 v를 큐에 삽입
    while len(queue) > 0:	        # 큐가 공백이 될 때까지 반복
        v = queue.popleft()		# 큐에서 정점 v 삭제
        for w in G[v]:			# v에 인접한 정점 w에 대해서
            if not visited[w]:		# 방문하지 않은 정점이면
                parent[w] = v           # 정점 v를 정점 w의 부모로 설정함
                visited[w] = True	# w를 방문한 것으로 기록
                queue.append(w)		# w를 큐에 삽입

def get_path(v):			# 종착점이 v인 최단 경로를 구하는 함수
    path = [v]				# 종착점을 삽입
    while parent[v] != -1:		# v가 루트가 될 때까지 반복
        v = parent[v]			# 부모 노드로 올라감
        path.append(v)			# path에 v를 추가함
    path.reverse()			# 역순으로 배치
    return path				# 최단 경로 리스트를 반환
    
def create_adj_list():
    n = int(input())		            # 정점 수
    m = int(input())		            # 에지 수
    G = [[] for _ in range(n)]	            # 인접 리스트를 위한 2차원 리스트
    for _ in range(m):		            # m개의 에지를 입력받음
        v, w = map(int, input().split())    # 에지 (v, w) 입력
        G[v].append(w)			    # v에 대한 리스트에 w 추가
        G[w].append(v)			    # w에 대한 리스트에 v 추가
    return G

# main program
G = create_adj_list()
visited = [False]*len(G)
parent = [-1]*len(G)
shortest_path(0)
print(parent)
path = get_path(6)
print(*path)

# 그래프 예
'''
8
11
0 2
0 3
0 4
1 2
1 4
1 5
2 4
2 7
3 7
5 6
5 7
'''
