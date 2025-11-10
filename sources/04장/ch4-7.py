"""프로그램 4.7: 무한 재귀에 빠진 프로그램의 예"""

def wrong_rsum(n):	# 종료 조건문이 누락된 재귀 함수
    return n + wrong_rsum(n)

def wrong(n):		# n이 짝수면 종료 조건에 도달하지 못함
    if n == 1:
        return 1
    else:
        return n + wrong(n-2)

