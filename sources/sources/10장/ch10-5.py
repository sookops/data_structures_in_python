"""프로그램 10.5: 힙에서 삽입을 수행하는 프로그램"""

def insert_heap(H, item):
    """힙 H에 새 원소 item을 삽입한다."""
    H.append(item)		# 새 원소를 리스트 맨 끝에 삽입
    i = len(H)-1    	        # i는 새 원소가 삽입된 위치(첨자)
    while i > 0:		# i가 루트가 아니면 반복함
        dad_i = (i-1) // 2	# dad_i는 i의 부모 위치
        if item <= H[dad_i]: 	# 우선순위가 같거나 더 큰 부모를 만나면
            break               # while 문을 빠져나감
        H[i] = H[dad_i]		# 부모 원소를 자식 위치로 옮김
        i = dad_i		# 부모 레벨로 이동
    H[i] = item			# 새 원소 저장

# 테스트
S = []
insert_heap(S, 5)
insert_heap(S, 25)
insert_heap(S, 10)
insert_heap(S, 20)
print(S)
