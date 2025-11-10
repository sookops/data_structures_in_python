import functools

@functools.lru_cache   #(maxsize=None)
def fib(n):
    """n번째 피보나치 수를 반환 - 지수 시간이 소요되는 재귀 함수"""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)	

import time
s = time.time()
print(fib(100))
t = time.time()
print(f"time = {(t-s):.3}")
