"""프로그램 12.6: 가중치 행렬 기반의 다익스트라 알고리즘의 구현"""

def dijkstra(M, src):
    """최단 경로를 구하는 다익스트라 알고리즘의 구현:
    가중치 행렬 M으로 표현된 가중치 그래프에서 출발점이 src인 최단 거리 리스트와 
    최단 경로 트리를 저장한 부모 포인터 배열을 반환한다."""
    n = len(M)	                    # 정점 수
    found = [False] * n	            # 최단 거리가 구해진 정점 집합 S
    dist = M[src].copy()	    # dist 초기화
    found[src] = True		    # 출발점을 집합 S에 포함
    parent = [src] * n	            # 부모 포인터 배열 초기화
    parent[src] = -1	            # 출발점 src를 루트로 설정

    for _ in range(n-2):	    # n-2번 반복
        v = -1                      # 선택할 정점 v
        minlength = float('inf')    # 최단 거리
        for w in range(n):	    # dist에서 최단 거리 검색
            if not found[w] and dist[w] < minlength:
                v, minlength = w, dist[w]
        found[v] = True		    # 정점 v의 최단 거리 구해짐
        for w in range(n):	    # dist 갱신
            if not found[w] and dist[w] > dist[v] + M[v][w]:
                dist[w] = dist[v] + M[v][w]
                parent[w] = v	# 최단 경로 트리 갱신

    return dist, parent	# 최단 거리와 최단 경로 트리 반환			    # 최소 신장 트리의 에지 리스트 반환

	
def create_cost_matrix():       # 가중치 행렬을 구축하는 함수, 방향 그래프
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    M = [[float('inf')]*n for _ in range(n)]	# 가중치 행렬의 초기화
    for v in range(n):                          # 주대각선은 0으로 설정
        M[v][v] = 0
    for _ in range(m):		                # m개 에지 입력받음
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        M[v][w] = c		                # 에지 가중치 설정
    return M				        # 가중치 행렬 반환

# main program
M = create_cost_matrix()

dist, parent = dijkstra(M, 0)
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
    
