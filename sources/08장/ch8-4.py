"""프로그램 8.4: 퀵 정렬의 분할 프로그램"""

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
