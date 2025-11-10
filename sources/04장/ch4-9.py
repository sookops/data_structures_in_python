"""프로그램 4.9: 하노이 탑 문제를 위한 재귀 함수"""

def hanoi(n, src, dest, other):
    """n개의 원반을 src에서 dest로 옮기는 절차를 출력한다"""
    if n == 1:			  # 종료 조건
        print(src, "->", dest)
    else:
        hanoi(n-1, src, other, dest)	  # src의 n-1개 원반을 other로 옮김
        print(src, "->", dest)		  # src에 남아 있는 원반을 dest로 옮김
        hanoi(n-1, other, dest, src)	  # other의 n-1개 원반을 dest로 옮김

# main program
hanoi(3, 'A', 'B', 'C')
