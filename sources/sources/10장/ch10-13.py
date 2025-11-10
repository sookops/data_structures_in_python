"""프로그램 10.13: 세그먼트 트리를 구축하는 프로그램"""

def build(i, start, end, D, T):
    """구간 합을 구하기 위한 세그먼트 트리를 구축한다."""
    if start == end:			# 잎 노드인 경우
        T[i] = D[start]
    else:
        mid = (start + end) // 2 	# 범위의 중앙 위치
        build(2*i+1, start, mid, D, T)	# 왼쪽 부트리 생성
        build(2*i+2, mid+1, end, D, T)	# 오른쪽 부트리 생성
        T[i] = T[2*i+1] + T[2*i+2]      # 합 계산
		
# 세그먼트 트리 T의 구축 테스트
D = [8, 1, 5, 4, 9, 7, 8, 2, 0, 5, 7, 2]    # 자료 원소
T = [None] * (4*len(D))			    # 0으로 초기화된 리스트
build(0, 0, len(D)-1, D, T)                 # 세그먼트 트리 구축
for x in T:
    if x: print(x, end=' ')
print()

D = [1, 3, 5, 7, 9, 11]
T = [None] * (4*len(D))			    # None으로 초기화된 리스트
build(0, 0, len(D)-1, D, T)                 # 세그먼트 트리 구축
for x in T:
    if x: print(x, end=' ')
print()
