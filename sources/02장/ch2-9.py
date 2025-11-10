"""프로그램 2.9: if-elif-else 문의 사용 예"""

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A 학점입니다.")				
elif score >= 80:
    print("B 학점입니다.")			
elif score >= 70:
    print("C 학점입니다.")			
else:
    print("F 학점입니다.")
