"""프로그램 4.2: 피보나치 수를 구하는 재귀 함수"""

def fib(n):
    """n번째 피보나치 수를 반환 - 지수 시간이 소요되는 재귀 함수"""
    if n <= 1:		            # 종료 조건
        return n
    else:
        return fib(n-1) + fib(n-2)  # 재귀 호출문

# main program
print(fib(5))
print(fib(10))
