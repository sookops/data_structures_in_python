"""프로그램 10.14: 세그먼트 트리에서 질의를 수행하는 프로그램"""

def build(i, start, end, D, T):
    """구간 합을 구하기 위한 세그먼트 트리를 구축한다."""
    if start == end:			# 잎 노드인 경우
        T[i] = D[start]
    else:
        mid = (start + end) // 2 	# 범위의 중앙 위치
        build(2*i+1, start, mid, D, T)	# 왼쪽 부트리 생성
        build(2*i+2, mid+1, end, D, T)	# 오른쪽 부트리 생성
        T[i] = T[2*i+1] + T[2*i+2]      # 합 계산

def query(i, start, end, left, right, T):
    """질의 구간 [left, right]의 합을 반환한다."""
    # 노드 구간과 질의 구간이 분리된 경우 (경우 1)
    if right < start or end < left:
        return 0
    # 노드 구간이 질의 구간에 포함되는 경우 (경우 2)
    if left <= start and end <= right:
        return T[i]
    # 노드 구간이 질의 구간을 포함하거나 부분적으로 교차하는 경우 (경우 3)
    mid = (start + end) // 2                                # 범위의 중앙 위치
    leftsum = query(2*i+1, start, mid, left, right, T)      # 왼쪽 부트리
    rightsum = query(2*i+2, mid+1, end, left, right, T)     # 오른쪽 부트리
    return leftsum + rightsum		                    # 합계 반환

# 테스트
D = [1, 3, 5, 7, 9, 11]                     # 자료 원소
T = [None] * (4*len(D))			    # None으로 초기화된 리스트
build(0, 0, len(D)-1, D, T)                 # 세그먼트 트리 구축
answer = query(0, 0, 5, 2, 4, T)	    # 질의 구간 [2, 4]
print(answer)

D = [8, 1, 5, 4, 9, 7, 8, 2, 0, 5, 7, 2]    # 자료 원소
T = [None] * (4*len(D))			    # None으로 초기화된 리스트
build(0, 0, len(D)-1, D, T)                 # 세그먼트 트리 구축
answer = query(0, 0, len(D)-1, 2, 4, T)	    # 질의 구간 [2, 4]
print(answer)
