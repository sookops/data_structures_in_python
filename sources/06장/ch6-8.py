"""프로그램 6.8: 미로에서 최단 경로를 구하는 프로그램"""

from collections import deque

def get_path(mark, enter, destination):
    print('get path')
    m, n = len(mark), len(mark[0])	# 미로의 행과 열의 크기
    x, y = destination			# 현재 위치, 목적지에서 시작
    path = []				# 최단 경로를 저장하는 리스트
    move_row = [-1, 0, 1, 0]		# 북, 동, 남, 서 방향의 행 첨자 변화
    move_col = [0, 1, 0, -1]		# 북, 동, 남, 서 방향의 열 첨자 변화

    while (x, y) != enter: 		# 입구에 도착할 때까지 탐색
        path.append((x, y))		# 현재 위치 저장
        for idx in range(4):		# 각 인접 위치 검사
            r = x + move_row[idx]	# 인접 위치 (r, c)
            c = y + move_col[idx]
            if not(0 <= r < m and 0 <= c < n):  # 미로 영역 벗어남
                continue
            if mark[r][c] == mark[x][y] - 1: 	# 이동 가능 위치
                x, y = r, c			# 현재 위치 갱신
                break

    path.append((x, y))			# 입구 위치 저장
    path.reverse()			# 입구부터 목적지까지의 경로 저장
    return path				# 최단 경로 반환

def find_shortest_path(maze, enter, destination):
    """미로 maze의 입구 enter에서 목적지 destination까지 경로가 존재하면
    입구부터 목적지까지 최단 경로 리스트를 반환하고, 없으면 None을 반환한다."""
    m, n = len(maze), len(maze[0])	# 미로의 행과 열의 크기
    mark = [[0]*n for _ in range(m)]	# mark 행렬 생성
    move_row = [-1, 0, 1, 0]		# 북, 동, 남, 서 방향의 행 첨자 변화
    move_col = [0, 1, 0, -1]		# 북, 동, 남, 서 방향의 열 첨자 변화
    Q = deque()				# deque를 이용한 큐 생성
    Q.append(enter)			# 큐에 입구 위치 삽입
    mark[enter[0]][enter[1]] = 1	# 입구 방문 기록

    while len(Q) > 0:			# 큐가 공백이 아니면 반복
        x, y = Q.popleft()		# 현재 위치 (x, y) (큐 삭제)
        if (x, y) == destination:	# 목적지 발견
            return get_path(mark, enter, destination)	# 최단 경로 반환
        for idx in range(4):    	# 각 인접 위치 검사
            r = x + move_row[idx]	# 인접 위치 (r, c)
            c = y + move_col[idx]
            if not(0 <= r < m and 0 <= c < n):      # 미로 영역 벗어남
                continue
            if maze[r][c] == 0 and mark[r][c] == 0: # 이동 가능 위치
                mark[r][c] = mark[x][y] + 1	    # mark 갱신
                Q.append((r, c))		    # 큐에 삽입

    return None     # 경로 존재하지 않음

# main program
M = [[0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 1, 0]]
enter = (0, 0)
dest = (3, 0)
print(*find_shortest_path(M, enter, dest))

M = [[0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 0]]
enter = (0, 0)
dest = (3, 4)
print(*find_shortest_path(M, enter, dest))
