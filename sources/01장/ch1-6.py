"""프로그램 1.6: 에라토스테네스의 체를 이용하여 소수의 개수를 세는 프로그램"""

def count_primes_era(n):
    """에라토스테네스의 체를 사용하여 구한 소수의 개수를 반환한다."""
    prime = [True] * (n+1)	            # True로 초기화된 리스트
    m = int(n ** 0.5)	    	            # n의 제곱근
    for i in range(2, m+1):
        if prime[i]:	                    # i가 소수인 경우
            for j in range(2*i, n+1, i):    # i를 제외한 i의 모든 배수에
                prime[j] = False            # False 배정
    return prime[2:].count(True)	    # True로 남아 있는 요소의 개수

# main program
n = int(input())
print(count_primes_era(n))
