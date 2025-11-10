"""프로그램 1.8: 지수 연산의 실행 시간"""

import time

start = time.time() 									# 시작 시간 기록
result = 10**5
stop = time.time()									# 종료 시간 기록
print("time1 =", round(stop-start, 3))	    # 실행 시간 출력

start = time.time() 									# 시작 시간 기록
result = 123456789**100000
stop = time.time()									# 종료 시간 기록
print("time2 =", round(stop-start, 3))	    # 실행 시간 출력
