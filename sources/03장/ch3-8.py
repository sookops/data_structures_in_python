"""프로그램 3.8: 문자열의 길이를 기준으로 하여 정렬을 수행하는 예"""

old_list = ['java', 'c', 'python', 'go']
new_list = sorted(old_list, key=len)	# len() 함수를 이용
print(new_list)	
