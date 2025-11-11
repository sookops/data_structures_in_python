"""프로그램 11.6: 모든 연결 요소를 출력하는 프로그램"""

# G : 파이썬 리스트로 구현된 인접 리스트 (전역 변수)
# visited : 정점 방문 여부를 기록하는 리스트, False로 초기화됨 (전역 변수)
# CC : 연결 요소에 포함되는 정점들을 저장하는 리스트 (전역 변수)

def visit(v):  			# dfs() 또는 bfs()에서 호출
    CC.append(v)		# v를 연결 요소에 추가
    
def dfs(v):
    visit(v)			# 정점 v에 특정 작업을 수행
    visited[v] = True		# 정점 v를 방문한 것으로 기록
    for w in G[v]:		# v에 인접한 정점 w에 대해서
        if not visited[w]:	# 방문하지 않은 정점이면
            dfs(w)		# w를 가지고 호출함

def all_components(n):		# 모든 연결 요소를 출력, n은 정점의 수
    for v in range(n):		# 각 정점 v에 대해서
        if not visited[v]:	# v를 아직 방문하지 않았으면 수행
            CC.clear()		# 리스트를 공백 상태로 설정함
            dfs(v)		# bfs()를 호출해도 됨
            print(*sorted(CC))	# 현재 연결 요소를 정렬하여 출력
			
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
CC = []
all_components(len(G))

# 그래프 예
'''
9
8
0 2
2 8
0 8
2 4
4 8
3 7
7 5
5 6
'''
