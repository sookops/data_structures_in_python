"""프로그램 2.23: 집합을 다루는 프로그램의 예"""

myset = {1, 6, 3, 8, 5, 1, 3, 8}    # set 객체 생성, 자동으로 중복을 제거함
print(myset)			    # 출력: {1, 3, 5, 6, 8} 
myset.add(4)			    # 요소 4를 삽입
myset.remove(1)			    # 요소 1을 삭제, 1이 없으면 오류 발생
myset.discard(6)		    # 요소 6을 삭제, 6이 없어도 오류 미발생
print(myset)			    # 출력: {3, 4, 5, 8}

set1 = {1, 2, 3}								
set2 = {3, 4, 5}
print(2 in set1, 3 not in set2)	    # 출력: True, False (멤버 검사)
print(set1 < set2)		    # 출력: False (부분집합 검사)
print(set1 & set2)		    # 출력: {3} (교집합 연산)
print(set1 | set2)		    # 출력: {1, 2, 3, 4, 5} (합집합 연산)
print(set1 - set2)		    # 출력: {1, 2} (차집합 연산)
