"""프로그램 2.21: 튜플을 다루는 프로그램의 예"""

numbers = (2, 7, 14, 26, 14)	    # 튜플 생성 - 소괄호 사용
names = "kim", "lee", "park" 	    # 튜플 생성 - 괄호 생략
print(numbers)			    # 출력: (2, 7, 14, 26, 14)
print(names)									# 출력: ('kim', 'lee', 'park')
x, y, z = names			    # 언패킹(unpacking)
print(x, y, z)			    # 출력: kim lee park
A = (1)											# 정수 1, 수식의 괄호로 인식
B = (1,)											# 1개 요소를 가진 튜플
print(numbers[1:3] + (2, 3))	    # 출력: (7, 14, 2, 3) 
print(numbers.index(14))	    # 출력: 2 (14의 최초 위치)
print(numbers.count(14))	    # 출력: 2 (14의 개수)
