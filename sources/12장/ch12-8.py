"""프로그램 12.8: 플로이드-와샬 알고리즘의 구현"""

def floyd(M):
    """플로이드-와샬 알고리즘의 구현:
    가중치 행렬 M으로 표현된 가중치 그래프에서 모든 정점 쌍의 최단 거리를 반환한다."""
    n = len(M)				# 정점 수
    A = [x.copy() for x in M]		# A의 초기화, M을 복사함
    for k in range(n):			# 최단 거리를 단계별로 구함
        for v in range(n):
            for w in range(n):
                A[v][w] = min(A[v][w], A[v][k]+A[k][w])
    return A			        # 최소 신장 트리의 에지 리스트 반환

	
def create_cost_matrix():       # 방향 그래프의 가중치 행렬을 구축하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    M = [[float('inf')]*n for _ in range(n)]	# 가중치 행렬의 초기화
    for v in range(n):                          # 주대각선은 0으로 설정
        M[v][v] = 0
    for _ in range(m):		                # m개 에지 입력
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        M[v][w] = c		                # 에지 가중치 설정
    return M				        # 가중치 행렬 반환

# main program
M = create_cost_matrix()

A = floyd(M)
for x in A:
    print(*x)

# 그래프 예
'''
4
8
0 1 30
0 2 25
0 3 40
1 2 -10
2 0 20
2 3 5
3 0 10
3 2 15
'''
    
