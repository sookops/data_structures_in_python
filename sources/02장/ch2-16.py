"""프로그램 2.16: break와 continue의 사용 예"""

for i in range(5):
    if i == 3:
        break 		# i가 3일 때 반복문 종료
    print(i) 		# 출력: 0, 1, 2

for i in range(5):
    if i == 3:
        continue 	# i가 3일 때 바로 다음 반복으로 넘어감
    print(i) 	        # 출력: 0, 1, 2, 4

