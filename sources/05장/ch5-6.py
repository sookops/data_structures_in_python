"""프로그램 5.6: 편집기 문제를 위한 파이썬 프로그램"""

left = list(input())	# 텍스트의 왼쪽 구간, 초기에 커서가 맨 끝에 있음
right = []		# 텍스트의 오른쪽 구간, 초기에 공백 리스트
n = int(input())	# 편집 명령의 개수

for _ in range(n):			# 편집 작업 수행
    op = input()			# 편집 명령 입력
    if op == 'L':			# 커서 왼쪽 이동
        if len(left) > 0:		# left가 공백이 아니면
            right.append(left.pop())	# left에서 삭제한 문자를 right에 삽입
    elif op == 'D':			# 커서 오른쪽 이동
        if len(right) > 0: 		# right가 공백이 아니면
            left.append(right.pop())	# right에서 삭제한 문자를 left에 삽입
    elif op == 'B':			# 커서 왼쪽 문자 삭제
        if len(left) > 0:
            left.pop()
    else:				# 'P $' 형태의 명령
        x, y = op.split()		# 삽입 명령 토큰 분리
        left.append(y)			# 커서의 왼쪽에 문자 삽입

right.reverse()				# right를 원래 순서로 바꿈
print(''.join(left+right))		# left와 right를 이어 붙인 문자열 출력

''' 입력 예 1 (답: abcdyx)
abcd
3
P x
L
P y
'''
''' 입력 예 2 (답: yxabc)
abc
9
L
L
L
L
L
P x
L
B
P y
'''
