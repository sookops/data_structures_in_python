"""프로그램 4.1: 등차수열의 합을 구하는 재귀 함수"""

def rsum(n):
    """1부터 n까지의 합을 반환하는 재귀 함수"""
    if n == 1: 		        # 종료 조건
        return 1
    else:
        return n + rsum(n-1)	# 재귀 호출문

# main program
print(rsum(10))
print(rsum(100))
