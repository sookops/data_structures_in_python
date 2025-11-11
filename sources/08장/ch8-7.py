"""프로그램 8.7: 기수 정렬"""

def radix_sort(S, M):
    """키의 범위가 [0, M-1]인 십진수들의 리스트 S를 정렬한다."""
    x = 1	    # 현재 처리할 자릿수 (1의 자리, 10의 자리, 100의 자리, ...)
    while x < M:
        B = [[] for _ in range(10)]	# 10개의 공백 버킷 생성
        for e in S:			# 분배 작업
            B[(e//x)%10].append(e)	# 현재 자릿수에 해당하는 버킷에 저장
        S.clear()			# S의 모든 요소 삭제
        for i in range(10):		# 수집 작업
            S.extend(B[i])		# 버킷의 요소들을 이어 붙임
        x *= 10								# 다음 자릿수로 이동

# main program
S = [304, 123, 212, 21, 321, 441, 343, 103]
radix_sort(S, 1000)
print(*S)
