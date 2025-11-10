"""프로그램 2.31: 클래스 정의와 사용 예 """

class Ball:			        # Ball 클래스 정의
    def __init__(self, pos=(0,0)):	# 메소드(객체 생성자)
        self.location = list(pos)	# 속성(인스턴스 변수) - 공 위치 좌표

    def move(self, dx, dy):		# 메소드 정의
        self.location[0] += dx		# 인스턴스 변수 참조
        self.location[1] += dy		# 공의 위치를 (dx, dy) 만큼 이동

# Ball 객체(인스턴스) 생성과 사용
a = Ball()			    # Ball 객체 생성, a.location -> [0, 0]
a.move(10, 5)			    # 메소드 호출, a.location -> [10, 5]
a.move(20, 15)			    # 메소드 호출, a.location -> [30, 20]
print(a.location)		    # 출력: [30, 20] (속성 참조)
b = Ball((5, 10))		    # Ball 객체 생성, b.location -> [5, 10]
b.location = [50, 50]		    # 속성 값 변경
print(b.location)		    # 출력: [50, 50]
