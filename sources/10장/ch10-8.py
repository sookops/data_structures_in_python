"""프로그램 10.8: 제자리 정렬 방식으로 동작하는 힙 정렬"""

def _heapify(H, n, root):   # root 위치 노드에 대해 힙 조정, n은 힙의 크기
    item = H[root]		# 옮겨질 원소
    i = root 			# i는 item을 저장할 위치
    son_i = 2*i + 1		# son_i는 i의 왼쪽 자식 위치
    while son_i < n:		# i가 잎 노드 위치가 아니면 반복함
        if son_i+1 < n and H[son_i] < H[son_i+1]:
            son_i += 1		# son_i에 우선순위가 더 큰 자식 위치 배정
        if item >= H[son_i]:	# 우선순위가 크거나 같으면 반복 중단
            break
        H[i] = H[son_i]		# 자식 원소를 부모 위치로 옮김
        i = son_i	        # 자식 레벨로 내려감
        son_i = 2*i + 1		# son_i를 i의 왼쪽 자식 위치로 갱신
    H[i] = item			# i 위치에 item 저장

def heap_sort(S):
    """힙 정렬로 리스트 S를 정렬한다."""
    for i in range((len(S)-1)//2, -1, -1):  # 힙 초기화
        _heapify(S, len(S), i)                 
        
    for i in range(len(S)-1, 0, -1):        # 힙의 크기가 1이 될 때까지 수행
        S[i], S[0] = S[0], S[i]             # 맨 앞 원소와 맨 끝 원소를 교환
        _heapify(S, i, 0)                   # 힙 조정

# 테스트
L = [20, 35, 25, 40, 15, 10, 30]
heap_sort(L)
print(*L)
