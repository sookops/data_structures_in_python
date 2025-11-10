"""프로그램 3.9: 정렬 기준을 제시하는 함수"""

def score(E):
    return -E[2]	# 세 번째 요소의 부호를 바꾸어 리턴

score_list = [(11, '홍길동', 95), (12, '박창호', 97), (15, '김철수', 89)]
score_list = sorted(score_list, key=score)
print(score_list)
