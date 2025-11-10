"""프로그램 6.3: Ο(n^2) 시간에 수행하는 프로그램"""

def num_interval(L, K):
    """리스트 L에서 부분합이 K인 구간의 개수를 반환한다."""
    count = 0				# 부분합이 K인 구간의 개수
    for s in range(len(L)):		# 부분합의 시작점 s
        sub_sum = 0			# 부분합의 시작점 s
        for t in range(s, len(L)):	# 부분합의 끝점 t 갱신
            sub_sum += L[t]		# 부분합에 구간의 맨 끝 숫자 더함
            if sub_sum == K:		# 부분합의 값이 K인 구간 찾음
                count += 1
            elif sub_sum > K:		# 부분합이 K보다 크면, 현재 시작점에서는
                break		        # 더 이상 탐색할 필요 없음
    return count		        # 부분합이 K인 구간 개수 반환

# main program
L = [3, 1, 4, 2, 1, 3, 1, 6]
K = 7
print(num_interval(L,K))

