"""프로그램 3.11: 두 개 이상의 기준을 가지고 정렬을 수행하는 예"""

data = [('kim', 5), ('lee', 4), ('park', 2), ('hong', 4), ('cho', 5)]
result = sorted(data, key=lambda E: (-E[1], E[0]))	
print(result)
