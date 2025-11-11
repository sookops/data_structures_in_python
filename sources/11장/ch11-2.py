"""프로그램 11.2: 무향 그래프의 인접 리스트를 구축하는 프로그램"""

def create_adj_list():          # 무향 그래프의 인접 리스트를 구축한 후 반환
    n = int(input())		            # 정점 수
    m = int(input())		            # 에지 수
    G = [[] for _ in range(n)]	            # 인접 리스트를 위한 2차원 리스트
    for _ in range(m):		            # m개의 에지를 입력받음
        v, w = map(int, input().split())    # 에지 (v, w) 입력
        G[v].append(w)			    # v에 대한 리스트에 w 추가
        G[w].append(v)			    # w에 대한 리스트에 v 추가
    return G				    # 인접 리스트 반환

# main program
G = create_adj_list()

for i in range(len(G)):
    print(i, ":", end=' ')
    for x in G[i]:
        print(x, end=' ')
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
