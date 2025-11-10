"""프로그램 12.9: AOV 네트워크에서 가장 빠른 완료 시간을 구하는 프로그램"""
							
def get_earliest_time(G, work_time):
    """AOV 네트워크에서의 가장 빠른 완료 시간:
    인접 리스트 G로 표현된 방향 비순환 그래프에서 각 작업의 가장 빠른 완료 시간을 
    저장한 리스트 earliest_time을 반환한다. G[v] = [인접 정점, ...],
    work_time[v] : 정점 v에 해당하는 작업의 소요 시간"""
    n = len(G)					# 정점 수
    earliest_time = work_time.copy()	        # earlist_time 초기화
    stack = []					# 공백 스택 생성, 리스트 이용
    indegree = [0] * n				# 전입 차수를 저장하는 리스트

    for v in range(n):				# 각 정점의 전입 차수를 구함
        for w in G[v]:
            indegree[w] += 1

    for v in range(n):				# 전입 차수가 0이면 스택에 삽입
        if indegree[v] == 0:
            stack.append(v)

    while len(stack) > 0:			# 스택이 공백이면 종료
        v = stack.pop()				# 스택의 top 정점 v 삭제
        for w in G[v]:				# 방향 에지 <v, w>에 대해
            t = earliest_time[v] + work_time[w]
            if t > earliest_time[w]: 		# early_time 갱신
                earliest_time[w] = t
                indegree[w] -= 1		# 전입 차수 1 감소
            if indegree[w] == 0: 		# 전입 차수가 0이면 스택에 삽입
                stack.append(w)

    return earliest_time			# 최단 완료 시간 반환			    # 최소 신장 트리의 에지 리스트 반환
	
def read_aov_network():         # AOV 네트워크의 입력을 수행하는 함수
    n = int(input())		                # 정점 수
    m = int(input())		                # 에지 수
    G = [[] for _ in range(n)]	                # 인접 리스트의 초기화
    for _ in range(m):		                # m개 에지 입력
        v, w = map(int, input().split())        # 에지 (v, w) 입력
        G[v].append(w)		                # v에 대한 리스트에 w 추가
    work_time = list(map(int, input().split())) # work_time 입력
    return G, work_time

# main program
G, work_time = read_aov_network()

earliest_time = get_earliest_time(G, work_time)
print('가장 빠른 시간 :', earliest_time)

# 그래프 예
'''
8
11
0 3
0 4
1 2
1 3
2 6
3 4
3 5
3 6
4 7
5 7
6 7
10 7 1 2 3 1 8 5
'''
    
