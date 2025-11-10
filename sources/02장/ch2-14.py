"""프로그램 2.14: while 문의 사용 예"""

count = 0
while count < 3:
    print(count)	    # 출력: 0, 1, 2
    count += 1

letter = input()
while letter != 'q':	    # 'q'가 입력될 때까지 입력된 문자열을 출력
    print(letter)
    letter = input()
