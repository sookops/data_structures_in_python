"""프로그램 11.1: 무향 그래프의 인접 행렬을 구축하는 프로그램"""

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

for i in range(len(M)):
    print(i,":", end=' ')
    for j in range(len(M)):
        if M[i][j] != 0: print(j, end=' ')
    print()
    
# 그래프 예
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
