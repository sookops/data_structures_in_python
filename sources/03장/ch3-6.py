"""프로그램 3.6: 삽입 정렬 알고리즘의 구현"""

def insertion_sort(L):
    """리스트 L의 요소들을 오름차순으로 정렬한다."""
    for k in range(1, len(L)):		# n-1번 반복, n = len(L)
        item = L[k]			# 삽입할 요소
        j = k-1				# 탐색의 시작 위치
        while j >= 0 and L[j] > item:	# 지배적 연산
            L[j+1] = L[j]		# item보다 큰 요소를 뒤로 이동
            j -= 1
        L[j+1] = item			# item 삽입

# main program
L = [65, 85, 55, 93, 35, 95, 87, 78]
insertion_sort(L)
print(*L)
