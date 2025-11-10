"""프로그램 11.3: 인접 행렬로 표현된 그래프에 대한 깊이 우선 탐색"""

# M : 2차원 리스트로 구현된 인접 행렬 (전역 변수)
# visited : 정점 방문 여부를 기록하는 리스트, False로 초기화됨 (전역 변수)

def visit(v):  			
    print(v, end=' ')
    
def dfs(v):
    visit(v)			# 정점 v에 특정 작업을 수행
    visited[v] = True		# 정점 v를 방문한 것으로 기록
    for w in range(len(M)):	# 모든 정점 w에 대해서
        if M[v][w] == 1 and not visited[w]:	# 방문하지 않은 인접한 정점
            dfs(w)		# w를 가지고 호출함

def create_adj_matrix():        # 무향 그래프의 인접 행렬을 구축한 후 반환
    n = int(input())		            # 정점 수
    m = int(input())		            # 에지 수
    M = [[0]*n for _ in range(n)]	    # 인접 행렬을 위한 2차원 리스트
    for _ in range(m):		            # m개의 에지를 입력받음
        v, w = map(int, input().split())    # 에지 (v, w) 입력
        M[v][w] = M[w][v] = 1		    # 양방향으로 1 설정
    return M				    # 인접 행렬 반환

# main program
M = create_adj_matrix()
visited = [False]*len(M)
dfs(0)
print()
visited = [False]*len(M)
dfs(4)
print()

'''
5	
6
0 1	
0 2	
1 2	
1 3	
1 4	
2 4	
'''
