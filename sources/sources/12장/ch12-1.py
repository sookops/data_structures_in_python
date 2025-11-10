"""프로그램 12.1: 가중치 무향 그래프의 가중치 행렬을 구축하는 프로그램"""

def create_cost_matrix():       # 가중치 행렬을 구축하는 함수
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

for i in range(len(M)):
    print(i,":", end=' ')
    for j in range(len(M)):
        if M[i][j] < float('inf'):
            print(f"({i}, {j} ; {M[i][j]})", end=' ')
    print()

# 그래프 예
'''
4
5
0 1 10
0 3 25
1 2 20
1 3 30
2 3 40
'''
    
