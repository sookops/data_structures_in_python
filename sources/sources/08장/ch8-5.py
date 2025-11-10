"""프로그램 8.5: 제자리 정렬을 위한 퀵 정렬"""

def partition(S, start, end):
    """리스트 S의 start부터 end까지의 구간을 분할한다."""
    pivot = S[end] 		        # 맨 끝 요소를 피벗으로 선택
    i = start-1 		        # 피벗보다 작은 요소의 마지막 첨자 저장
    for j in range(start, end):
        if S[j] < pivot:        	# 피벗보다 작으면
            i += 1 		        # 피벗보다 작은 요소 추가됨
            S[i], S[j] = S[j], S[i]	# S[i]와 S[j]를 교환함

    S[i+1], S[end] = S[end], S[i+1]	# S[i+1]과 S[end]를 교환함
    return i+1				# 피벗의 최종 위치(첨자) 반환

def quicksort(S, start, end):
    """퀵 정렬 알고리즘으로 리스트 S를 정렬한다."""
    if start >= end: 			# 정렬 범위가 1 이하이면 작업 종료
        return
    pos = partition(S, start, end)	# 리스트 분할
    if pos-start < end-pos:		# 왼쪽 구간의 크기가 더 작으면
        quicksort(S, start, pos-1)	# 왼쪽 구간부터 정렬
        quicksort(S, pos+1, end)
    else:				# 오른쪽 구간의 크기가 더 작으면
        quicksort(S, pos+1, end)	# 오른쪽 구간부터 정렬
        quicksort(S, start, pos-1)

# main program
S = [35, 55, 65, 78, 85, 87, 93, 95]
quicksort(S, 0, len(S)-1)
print(*S)
