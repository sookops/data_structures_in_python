"""프로그램 2.22: 딕셔너리를 다루는 프로그램의 예"""

person = { 'name': 'kim', 'age': 20, 'city': 'busan' }
print(f"이름: {person['name']}") 	# 출력: kim (값에 접근)
person['job'] = 'student'		# 새로운 요소 삽입
person['age'] = 21			# 기존 값 변경
del person['city']			# 키를 가지고 요소 삭제
print(person)		# 출력: {'name': 'kim', 'age': 21, 'job': 'student'}
print(*person)				# 출력: name age job (키만 출력)
if 'city' not in person:		# 키 비포함 검사 (not in)
    person['city'] = 'incheon'		# 새로운 요소 삽입
for key in person:			# for 문에서 모든 키 검사
    print(person[key], end=' ')		# 출력: kim 21 student incheon
