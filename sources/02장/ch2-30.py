"""프로그램 2.30: __main__ 모듈인 경우에만 실행되는 코드를 가진 프로그램의 예 """

# my_module.py
def my_function():
    print("모듈의 함수가 실행되었습니다.")

if __name__ == "__main__":
    # 이 부분은 my_module.py가 직접 실행될 때만 동작합니다.
    print("__main__ 모듈로 실행되었습니다.")
    my_function()
