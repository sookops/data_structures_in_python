"""프로그램 4.5: 피보나치 수를 구하는 새로운 재귀 함수"""

def nfib(n):
    """n번째와 n-1번째 피보나치 수를 반환 – 선형 시간에 수행하는 재귀 함수"""
    if n <= 1:			# 종료 조건
        return (n, 0)		# (0, 0) 또는 (1, 0) 반환
    else:
        (a, b) = nfib(n-1)	# a = F(n-1), b = F(n-2)
        return (a+b, a)		# (F(n), F(n-1))을 반환

# main program
print(nfib(10)[0])
print(nfib(100)[0])
