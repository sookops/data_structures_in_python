"""프로그램 2.27: 람다 함수의 예"""

is_even = lambda x: x % 2 == 0	    # 람다 함수 (짝수 검사)
print(is_even(5))		    # 출력: False
print(is_even(8))		    # 출력: True

acc = lambda x, y=1: x + y	    # 람다 함수 (디폴트 인수 사용)
print(acc(2, 3))		    # 출력: 5
print(acc(5))			    # 출력: 6 
