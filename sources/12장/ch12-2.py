"""프로그램 12.2: 가중치 무향 그래프의 인접 리스트를 구축하는 프로그램"""

def create_weighted_adj_list():       # 가중치 인접 리스트를 구축하는 함수
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

for i in range(len(G)):
    print(i,":", end=' ')
    for x in G[i]:
        print(f"({i}, {x[0]} ; {x[1]})", end=' ')
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
    
