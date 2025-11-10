"""프로그램 4.3: 피보나치 수를 구하는 반복 구조 프로그램"""

def iterfib(n):
    """n번째 피보나치 수를 반환 - 선형 시간에 수행하는 반복 구조 프로그램"""
    if n <= 1: 		                # F(0) = 0, F(1) = 1
        return n
    curr, prev = 1, 0		        # curr = F(1), prev = F(0)
    for i in range(2, n+1):	        # F(2)부터 F(n)까지 차례로 구함
        curr, prev = curr+prev, curr	# curr = F(i), prev = F(i-1)
    return curr				# F(n)

# main program
print(iterfib(10))
print(iterfib(100))
