"""프로그램 11.8: 위상 정렬을 수행하는 프로그램"""

def topologicalSort(G):
    """인접 리스트 G로 표현된 방향 비순환 그래프에서 구한 위상 순서를 반환한다."""
    n = len(G)				# 정점의 개수
    toseq = []				# 위상 순서를 저장하는 리스트
    indeg = [0] * n			# 전입 차수를 저장하는 리스트
    stack = []				# 공백 스택 생성 (리스트 이용)
    for v in range(n):			# 각 정점의 전입 차수를 구함
        for w in G[v]:
            indeg[w] += 1
    for v in range(n):			# 전입 차수가 0인 정점을 스택에 삽입
        if indeg[v] == 0:
            stack.append(v)
    while len(stack) > 0:		# 스택이 공백이 될 때까지 반복
        v = stack.pop()			# 스택의 top 정점 v 삭제
        toseq.append(v)			# 위상 순서에 정점 v 추가
        for w in G[v]:			# 방향 에지 <v, w>에 대해
            indeg[w] -= 1		# 전입 차수 1 감소
            if indeg[w] == 0: 		# 전입 차수가 0이면 스택에 삽입
                stack.append(w)
    return toseq			# 위상 순서 반환
    
def create_adj_list():
    n = int(input())		            # 정점 수
    m = int(input())		            # 에지 수
    G = [[] for _ in range(n)]	            # 인접 리스트를 위한 2차원 리스트
    for _ in range(m):		            # m개의 에지를 입력받음
        v, w = map(int, input().split())    # 방향 에지 <v, w> 입력
        G[v].append(w)			    # v에 대한 리스트에 w 추가
    return G

# main program
G = create_adj_list()
print(*topologicalSort(G))

# 그래프 예
'''
7
9
0 5
1 3
1 4
3 2
3 4
2 5
2 6
4 6
5 6
'''
