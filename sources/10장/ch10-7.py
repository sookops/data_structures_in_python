"""프로그램 10.7: 힙 초기화와 삭제를 수행하는 프로그램"""

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

def _fix_heap(H, root):		# root 위치의 노드에 대해 하향식 힙 조정
    item = H[root]		# 옮겨질 원소
    i = root			# item을 저장할 위치
    son_i = 2*i + 1 	        # son_i는 i의 왼쪽 자식 위치
    while son_i < len(H):	# i가 잎 노드 위치가 아니면 반복함
        if son_i+1 < len(H) and H[son_i] < H[son_i+1]:
            son_i += 1		# son_i에 우선순위가 더 큰 자식 위치 배정
        if item >= H[son_i]:	# 자식보다 우선순위가 크거나 같으면 반복 중단
            break
        H[i] = H[son_i]		# 자식 원소를 부모 위치로 옮김
        i = son_i		# 자식 레벨로 내려감
        son_i = 2*i + 1		# son_i를 i의 왼쪽 자식 위치로 갱신
    H[i] = item		        # i 위치에 item 저장

def delete_heap(H):
    """힙 H에서 루트 원소를 삭제한 후 반환한다."""
    if len(H) == 0:     	# 공백 상태에서 호출되면 None을 반환
        return None
    if len(H) == 1:             # 원소가 하나만 있는 경우, 원소 삭제 후 반환
        return H.pop()          # 힙 조정이 필요 없음
    del_item = H[0]		# 삭제 후 반환할 요소
    H[0] = H.pop()		# 마지막 요소를 삭제하고 루트로 옮김
    _fix_heap(H, 0)     	# 루트 노드에 대해 힙 조정
    return del_item             # 삭제된 원소 반환

def init_heap(H):
    """리스트 H를 힙으로 초기화한다."""
    for i in range((len(H)-1)//2, -1, -1):	# H[i]가 루트인 부트리를
        _fix_heap(H, i) 			# 힙으로 조정
    
# 테스트
S = [20, 35, 25, 40, 15, 10, 30]
init_heap(S)
print(S)

for _ in range(len(S)):
    print(delete_heap(S))
    print(S)
    
