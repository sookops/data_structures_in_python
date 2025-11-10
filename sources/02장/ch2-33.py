"""프로그램 2.33: 내부 클래스 정의와 사용 예"""

class OutClass:				        # 외부 클래스 정의
    class InClass:			        # 내부 클래스 정의
        def __init__(self):	                # 내부 클래스 생성자
            print("내부 클래스 인스턴스 생성")

        def in_method(self):		        # 내부 클래스 메소드
            print("내부 클래스 메소드 호출")

    def __init__(self):			        # 외부 클래스 생성자
        self.in_obj = self.InClass()	        # 내부 클래스 인스턴스 생성

    def out_method(self):		        # 외부 클래스 메소드
        self.in_obj.in_method()		        # 내부 클래스 메소드 호출

out_obj = OutClass()			        # 외부 클래스 인스턴스 생성
out_obj.out_method()			        # 외부 클래스 메소드 호출
new_in_obj = OutClass.InClass()		        # 직접 내부 클래스 인스턴스 생성
new_in_obj.in_method()			        # 내부 클래스 메소드 호출
