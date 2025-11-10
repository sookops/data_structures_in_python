"""프로그램 1.2: 최대공약수를 구하는 파이썬 프로그램 (재귀 함수)"""

def gcd(one, two):
    """두 자연수 one과 two의 최대공약수를 반환한다."""
    if two == 0: return one
    return gcd(two, one % two)	

# main program
print(gcd(24, 18))
print(gcd(1098021, 8808825))
