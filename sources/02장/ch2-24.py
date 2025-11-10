"""프로그램 2.24: 사용자 정의 함수의 예"""

# 함수 정의
def greet(name):					# 함수 머리
    """주어진 이름을 가진 사람에게 인사하는 함수"""	# 함수 몸체
    return f"안녕하세요, {name}!"

message = greet("홍길동")		# 함수 호출
print(message)				# 출력: 안녕하세요, 홍길동!
