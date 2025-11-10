"""프로그램 2.26: 다양한 매개변수 전달 방식을 사용하는 프로그램의 예"""

def greet(name, msg='Hello'):		# 디폴트 인자를 가진 함수
    print(f"안녕 {name}, {msg}")

def square_sum(*numbers):		# 가변 인자를 가진 함수
    total = 0
    for x in numbers:			# numbers는 튜플
        total += x*x
    print(total)

greet('길동')				# 출력: 안녕 길동, Hello
greet(msg="좋은 아침!", name="길동")	# 출력: 안녕 길동, 좋은 아침!
square_sum(1, 2)	    		# 출력: 5
square_sum(1, 2, 3, 4, 5)		# 출력: 55
