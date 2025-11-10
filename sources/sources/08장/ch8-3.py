"""프로그램 8.3: 퀵 정렬"""

def quick_sort(S):
    """퀵 정렬 알고리즘으로 리스트 S를 정렬한다."""
    if len(S) <= 1: 	        # 길이가 1 이하이면 작업 종료
        return

    L, C, R = [], [], []
    pivot = S[0]        	# 첫 번째 요소를 피벗으로 선택
    for x in S:			# 리스트 분할
        if x < pivot:
            L.append(x)
        elif x > pivot:
            R.append(x)
        else:
            C.append(x)

    quick_sort(L)		# L의 정렬
    quick_sort(R)		# R의 정렬
    S[:] = L + C + R		# 리스트 이어 붙임

# main program
S = [35, 55, 65, 78, 85, 87, 93, 95]
quick_sort(S)
print(*S)
