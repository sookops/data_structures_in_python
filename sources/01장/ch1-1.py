"""프로그램 1.1: 최대공약수를 구하는 파이썬 프로그램 (반복 구조)"""

def gcd(one, two):
    """두 자연수 one과 two의 최대공약수를 반환한다."""
    while two > 0:
        one, two = two, one % two
    return one

# main program
print(gcd(24, 18))
print(gcd(1098021, 8808825))
