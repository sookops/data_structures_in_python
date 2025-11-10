"""프로그램 2.29: 다양한 방식으로 모듈을 불러오는 프로그램의 예 """

from sys import *		# sys 모듈의 모든 기능을 불러옴
from math import pi, sqrt	# math 모듈에서 pi와 sqrt() 함수를 불러옴
import time as t		# time 모듈의 별칭으로 t를 설정 
print(pi, sqrt(2))		# 원주율과 2의 제곱근 출력 (모듈명 생략)
print(t.ctime())		# 현재 시간 출력 (별칭 사용)
exit()				# 프로그램 종료 (모듈명 생략)
