"""프로그램 1.5: 일반적인 소수 판별 방식으로 소수의 개수를 세는 프로그램"""

def is_prime(x):
    """x가 소수이면 True, 아니면 False를 반환한다."""
    m = int(x ** 0.5)		# x의 제곱근
    for i in range(2, m+1):
        if x % i == 0:          # 약수 발견
            return False
    return True

def count_primes_normal(n):
    """n 이하의 소수 개수를 반환한다."""
    count = 0
    for x in range(2, n+1):
        if is_prime(x):
            count += 1
    return count

# main program
n = int(input())
print(count_primes_normal(n))
