"""프로그램 8.2: 합병을 수행하는 프로그램"""

def merge(S, L, R):
    """두 정렬된 리스트 L과 R을 합병하여 정렬된 리스트 S를 구축한다."""
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            S[i+j] = L[i]	# L[i]가 S의 다음 요소가 됨
            i += 1
        else:
            S[i+j] = R[j]	# R[j]가 S의 다음 요소가 됨
            j += 1

    while i < len(L):		# L에 남아 있는 요소를 S에 배정함
        S[i+j] = L[i]
        i += 1

    while j < len(R):		# R에 남아 있는 요소를 S에 배정함
        S[i+j] = R[j]
        j += 1
		
def merge_sort(S):
    """합병 정렬 알고리즘으로 리스트 S를 정렬한다."""
    if len(S) <= 1:     # 길이가 1 이하이면 작업 종료 (종료 조건)
        return
    mid = len(S) // 2	# 중앙 위치 계산
    L = S[:mid]		# S의 왼쪽 구간 (새로운 리스트 생성)
    R = S[mid:]         # S의 오른쪽 구간 (새로운 리스트 생성)
    merge_sort(L)	# 리스트 L의 정렬 (재귀 호출)
    merge_sort(R)	# 리스트 R의 정렬 (재귀 호출)
    merge(S, L, R)	# L과 R을 합병하여 정렬된 리스트 S를 구함

# main program
S = [35, 55, 65, 78, 85, 87, 93, 95]
merge_sort(S)
print(*S)
