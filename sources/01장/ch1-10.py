"""프로그램 1.10: 순차 탐색 알고리즘"""

def seq_search(L, item):
    """리스트 L에서 item의 최소 위치를 반환한다."""
    for i in range(len(L)):
        if L[i] == item:
            return i
    return None

# main program
L = [5, 9, 3, 1, 2, 7, 8, 4]
print(seq_search(L, 3))
print(seq_search(L, 6))
