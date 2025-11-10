"""프로그램 2.11: 윤년 여부를 판별하는 조건문"""

year = int(input("연도를 입력하세요 : "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("윤년입니다.")				
else:
    print("평년입니다.")	
