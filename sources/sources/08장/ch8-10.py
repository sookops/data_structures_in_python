"""프로그램 8.10: 반딧불이 문제를 위한 파이썬 프로그램"""

from bisect import *

N, H = map(int, input().split())    # 동굴의 길이와 높이
A, B = [], []			    # 석순과 종유석 리스트
for _ in range(N//2):		    # 석순과 종유석 높이 입력
    A.append(int(input()))	    # 석순 입력
    B.append(int(input()))	    # 종류석 입력

A.sort()			    # 석순 높이의 오름차순 정렬			
B.sort()			    # 종유석 높이의 오름차순 정렬
min_obs = N			    # 파괴할 장애물의 최소 개수
count = 1			    # 최소 개수의 장애물을 파괴하는 구간의 수

for y in range(H):		    # 각 높이 구간에 대해서
    a = bisect_left(A, y+1)	    # A에서 파괴되는 석순의 최초 위치
    b = bisect_left(B, H-y)	    # B에서 파괴되는 종유석의 최초 위치
    num = N-a-b			    # 파괴되는 장애물의 수
    if num < min_obs:  		    # 파괴되는 장애물의 수가 더 작은 구간 발견
        min_obs = num
        count = 1
    elif num == min_obs: 	    # 최소 개수의 장애물을 파괴하는 구간 발견
        count += 1

print(min_obs, count)	            # 장애물 개수와 구간의 수 출력

