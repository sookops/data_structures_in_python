"""프로그램 6.7: mark 행렬로부터 경로를 추출하는 프로그램"""

def get_path(mark, enter, destination):
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

 
