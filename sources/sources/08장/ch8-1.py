"""프로그램 8.1: 합병 정렬"""

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
