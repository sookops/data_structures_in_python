"""프로그램 1.11: 다양한 시간복잡도 분석을 위한 프로그램 예"""

def program_A(n):	    # 프로그램 A
    countA = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                countA += 1
    return countA

def program_B(n):	    # 프로그램 B
    countB = 0
    for i in range(n):
        for j in range(i, n):
            countB += 1
    return countB

def program_C(n):	    # 프로그램 C
    countC = 0
    for i in range(n):
        j = n
        while j >= 1:
            countC += 1
            j //= 2
    return countC

def program_D(n):	    # 프로그램 D
    countD = 0
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            countD += 1
    return countD
    
# main program
n = int(input())
print("A =", program_A(n))
print("B =", program_B(n))
print("C =", program_C(n))
print("D =", program_D(n))

