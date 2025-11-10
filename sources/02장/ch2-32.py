"""프로그램 2.32: 클래스 속성 정의와 사용 예"""

class Ball:				# Ball 클래스 정의
    owner = "kim" 			# 클래스 속성

    def __init__(self, pos=(0,0)):
        self.location = list(pos)	# 인스턴스 속성

    def move(self, dx, dy):
        self.location[0] += dx
        self.location[1] += dy				

# Ball 객체(인스턴스) 생성과 사용
a = Ball()								
b = Ball((5, 10))
print(a.owner, b.owner)		# 출력: kim kim (클래스 속성 참조)
Ball.owner = "lee" 		# 클래스 속성 변경
print(a.owner, b.owner)		# 출력: lee lee (클래스 속성 참조)
