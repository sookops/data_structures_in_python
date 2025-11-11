"""프로그램 12.3: 가중치 행렬 기반의 프림 알고리즘의 구현"""

def prim(M):
    """프림 알고리즘의 구현:
    가중치 행렬 M으로 표현된 가중치 그래프에서 최소 신장 트리의 에지 리스트를 
    반환한다."""
    n = len(M)			            # 정점 수
    mst = []		                    # 최소 신장 트리의 에지 리스트
    nearest = [0] * n		            # 가장 가까운 정점 리스트
    selected = [False] * n	            # 트리 정점이면 True, 아니면 False
    selected[0] = True		            # 시작 정점 0을 트리 정점으로 설정

    while len(mst) < n-1:	            # n-1개의 에지를 선택할 때까지 반복
        w, mincost = -1, float('inf')	    # 선택할 비트리 정점 w와 가중치
        for v in range(n):		    # 가중치가 최소인 에지 탐색
            if not selected[v] and M[v][nearest[v]] < mincost:
                w, mincost = v, M[v][nearest[v]]
        if w == -1: 		            # MST가 존재하지 않으면 None 반환
            return None
        selected[w] = True	            # w를 트리 정점으로 설정
        mst.append((nearest[w], w, M[nearest[w]][w]))    # 트리 에지 추가
        for v in range(n):		    # nearest 갱신
            if not selected[v] and M[v][w] < M[v][nearest[v]]:
                nearest[v] = w

    return mst				    # 최소 신장 트리의 에지 리스트 반환

def create_cost_matrix():       # 무향 그래프의 가중치 행렬을 구축하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    M = [[float('inf')]*n for _ in range(n)]	# 가중치 행렬의 초기화
    for v in range(n):                          # 주대각선은 0으로 설정
        M[v][v] = 0
    for _ in range(m):		                # m개 에지 입력
        v, w, c = map(int, input().split())     # 에지 (v, w) 가중치 c 입력
        M[v][w] = M[w][v] = c		        # 에지 가중치 설정
    return M				        # 가중치 행렬 반환

# main program
M = create_cost_matrix()

A = prim(M)
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
    
