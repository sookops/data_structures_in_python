"""프로그램 2.10: 윤년 여부를 판별하는 중첩된 조건문"""

year = int(input("연도를 입력하세요 : "))

if year % 400 == 0:
    print("윤년입니다.")				
else:
    if year % 4 == 0:
        if year % 100 != 0:
            print("윤년입니다.")
        else:
            print("평년입니다.")
    else:
        print("평년입니다.")
