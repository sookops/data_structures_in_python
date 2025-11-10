"""프로그램 1.7: 에라토스테네스의 체 알고리즘의 실행 시간 측정"""

import time

def count_primes_era(n):
    """에라토스테네스의 체를 사용하여 구한 소수의 개수를 반환한다."""
    prime = [True] * n		        # True로 초기화된 리스트
    m = int(n ** 0.5)	    	        # n의 제곱근
    for i in range(2, m+1):
        if prime[i]:	                # i가 소수인 경우
            for j in range(2*i, n, i):	# i의 배수에 False 배정
                prime[j] = False
    return prime[2:].count(True)	# True로 남아 있는 요소의 개수

# main program		
n = int(input())
start = time.time() 								# 시작 시간 기록
print(count_primes_era(n))		# 함수 countPrimes_era() 호출 
stop = time.time()								# 종료 시간 기록
print("time =", round(stop-start, 3))	# 소수점 셋째 자리까지 출력

