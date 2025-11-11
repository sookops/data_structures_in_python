"""프로그램 8.6: 버킷 정렬"""

def key(e):     # 요소 e의 키를 반환
    return e

def bucket_sort(S, M):
    """키의 범위가 [0, M-1]인 요소들의 리스트 S를 정렬한다."""
    B = [[] for _ in range(M)]	    # M개의 공백 버킷 생성
    for e in S: 		    # S의 요소들을 해당 버킷에 저장
        B[key(e)].append(e)	    # key(e)는 e의 키를 의미함
    S.clear()			    # S의 모든 요소 삭제 – 버킷 비움
    for i in range(M):              # 버킷의 요소들을 S에 이어 붙임
        S.extend(B[i])

# main program
S = [35, 55, 65, 78, 85, 87, 93, 95]
bucket_sort(S, 100)
print(*S)
