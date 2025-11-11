"""프로그램 8.9: 퀵 선택"""

import random

def quick_select(S, k):
    """리스트 S에서 k번째 작은 요소를 반환한다. 0 <= k < len(S)."""
    if not (0 <= k < len(S)): 	    # k가 유효한 값이 아니면 –1을 반환
        return -1
    if len(S) == 1: 		    # 길이가 1 이하이면 작업 종료
        return S[0]

    L, C, R = [], [], []
    pivot = random.choice(S)	    # 피벗을 무작위로 선택함 (random 모듈)
    for x in S:		    	    # 리스트 분할
        if x < pivot:
            L.append(x)
        elif x > pivot:
            R.append(x)
        else:
            C.append(x)

    if k < len(L): 		    # k번째 작은 요소는 L에 존재함
        return quick_select(L, k)   # 재귀 호출 (L에서 탐색)
    elif k < len(L)+len(C):         # k번째 작은 요소는 피벗임
        return pivot	            # k번째 작은 요소 반환
    else: 	                    # k번째 작은 요소는 R에 존재함
        return quick_select(R, k-len(L)-len(C))	    # 재귀 호출 (R에서 탐색)

# main program
L = [5, 12, 18, 25, 25, 25, 30, 30, 32, 38]
print(quick_select(L, 5))
print(quick_select(L, 8))
print(quick_select(L, 10))
