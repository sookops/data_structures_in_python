"""프로그램 3.4: 선택 정렬 알고리즘의 구현"""

def selection_sort(L):
    """리스트 L의 요소들을 오름차순으로 정렬한다."""
    n = len(L)			        # 요소의 개수
    for start in range(n-1):	        # start - 정렬 범위의 시작 위치
        minPos = start
        for j in range(start+1, n):	# 가장 작은 요소 위치 탐색
            if L[j] < L[minPos]:	# 시간복잡도 분석을 위한 지배적 연산
                minPos = j
        L[minPos], L[start] = L[start], L[minPos]   # 요소 교환

# main program
L = [65, 85, 55, 93, 35, 95, 87, 78]
selection_sort(L)
print(*L)
