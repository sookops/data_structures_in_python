"""프로그램 5.5: 미로 문제를 위한 파이썬 프로그램"""

def find_path(maze, enter, destination):
    """스택을 이용하여 미로에서 길을 찾는 프로그램:
    미로 maze의 입구 enter에서 목적지 destination까지 경로가 존재하면
    입구부터 목적지까지 경로 리스트를 반환하고, 없으면 None을 반환한다."""
    m, n = len(maze), len(maze[0])	# 미로의 행과 열의 크기
    mark = [[0]*n for _ in range(m)]	# mark 생성
    move_row = [-1, 0, 1, 0]
    move_col = [0, 1, 0, -1]
    stack = []				# 공백 스택 생성
    stack.append(enter)			# 스택에 입구 좌표 삽입
    mark[enter[0]][enter[1]] = 1	# 입구 방문 기록

    while len(stack) > 0:		# 스택이 공백이 아니면 반복함
        x, y = stack[-1]		# 현재 위치 (x, y)
        if (x, y) == destination:	# 목적지 도달
            return stack		# 입구에서 목적지까지의 경로 반환
        found_next_move = False		# 이동 가능한 인접 위치 발견 여부
        for idx in range(4):		# 각 인접 위치 검사
            r = x + move_row[idx]	# 인접 위치 (r, c)
            c = y + move_col[idx]
            if not(0 <= r < m and 0 <= c < n):      # 미로 영역 벗어남
                continue        
            if maze[r][c] == 0 and mark[r][c] == 0: # 이동 가능 위치
                stack.append((r, c))
                mark[r][c] = 1
                found_next_move = True
                break
        if not found_next_move:	        # 이동 가능한 위치가 없으면
            stack.pop()		        # 직전 위치로 후퇴함

    return None			        # 목적지까지 경로가 존재하지 않음

# main program
M = [[0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 1, 0]]
enter = (0, 0)
dest = (3, 0)
print(*find_path(M, enter, dest))
