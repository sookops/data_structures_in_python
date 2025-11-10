"""프로그램 4.10: 이진 탐색을 수행하는 재귀 함수"""

def bin_search(L, low, high, x):
    """L에서 탐색값 x의 위치(첨자)를, 탐색에 실패하면 None을 반환한다."""
    if low > high:		# 종료 조건 – 공백인 탐색 구간
        return None		# 탐색 실패
    else:
        mid = (low + high) // 2		# 중앙 위치 계산
        if x == L[mid]: 	        # 탐색 성공
            return mid
        elif x < L[mid]:
            return bin_search(L, low, mid-1, x)	    # 왼쪽 구역 탐색
        else:
            return bin_search(L, mid+1, high, x)    # 오른쪽 구역 탐색

# main program
L = [12, 18, 33, 34, 40, 52, 56, 78, 87]
print(bin_search(L, 0, len(L)-1, 33))
print(bin_search(L, 0, len(L)-1, 89))
