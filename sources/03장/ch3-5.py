"""프로그램 3.5: 버블 정렬 알고리즘의 구현"""

def bubble_sort(L):
    """리스트 L의 요소들을 오름차순으로 정렬한다."""
    n = len(L)				# 요소의 개수
    for end in range(n, 1, -1):		# end - 작업 범위의 끝 + 1
        for j in range(1, end):
            if L[j-1] > L[j]:		        # 지배적 연산
                L[j-1], L[j] = L[j], L[j-1]	# 요소 교환

# main program
L = [65, 85, 55, 93, 35, 95, 87, 78]
bubble_sort(L)
print(*L)
