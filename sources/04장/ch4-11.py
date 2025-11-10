"""프로그램 4.11: 이진 탐색을 수행하는 반복 구조 프로그램"""

def bin_search_iter(L, x):
    """L에서 탐색값 x의 위치(첨자)를, 탐색에 실패하면 None을 반환한다."""
    low, high = 0, len(L)-1	    # 탐색 범위 지정
    while low <= high: 		    # 탐색 구간이 공백이 아니면 반복함
        mid = (low + high) // 2	    # 중앙 위치 계산
        if x == L[mid]: 	    # 탐색 성공
            return mid
        elif x < L[mid]: 	    # 왼쪽 구역 탐색
            high = mid-1
        else: 		            # 오른쪽 구역 탐색
            low = mid+1
    return None	                    # 탐색 실패								# 탐색 실패

# main program
L = [12, 18, 33, 34, 40, 52, 56, 78, 87]
print(bin_search_iter(L, 33))
print(bin_search_iter(L, 89))
