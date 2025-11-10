"""프로그램 1.3: 반복문을 이용하여 1부터 n까지의 합을 계산하는 프로그램"""

n = int(input())
total = 0		
for x in range(1, n+1):
    total += x
print("sum =", total)
