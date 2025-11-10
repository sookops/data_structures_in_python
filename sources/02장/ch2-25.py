"""프로그램 2.25: 함수 내부에서 전역 변수를 사용하는 프로그램의 예"""

y = 20  		    # y는 전역 변수
name = ['kim', 'lee']	    # name은 전역 변수

def f(x):		    # 매개변수 x는 지역 변수
    print(x+y)  	    # 함수 내부에서 전역 변수 읽기

def g():
    global y 		    # y를 전역 변수로 선언
    y = 30  		    # 전역 변수 y의 값을 변경
    name.append('park')	    # 리스트 name에 요소 추가

f(10) 			    # 출력: 30
g()							
print(y)           	    # 출력: 30
print(*name)		    # 출력: kim lee park
