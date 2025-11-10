"""프로그램 3.10: lambda 함수를 활용하여 정렬을 수행하는 예"""

score_list = [(11, '홍길동', 95), (12, '박창호', 97), (15, '김철수', 89)]
score_list = sorted(score_list, key=lambda E: -E[2])
print(score_list)
