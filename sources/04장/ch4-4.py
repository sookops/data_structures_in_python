"""프로그램 4.4: 피보나치 수를 구하는 메모이제이션을 도입한 재귀 함수"""

def mfib(n, F = [0, 1]):
    """n번째 피보나치 수를 반환 - 메모이제이션 기법으로 선형 시간에 수행하는 재귀 함수
    최초 호출 전에 F = [0, 1]로 초기화됨"""
    if n < len(F):		# 종료 조건 – 계산 결과가 저장된 경우
        return F[n]		# 저장된 피보나치 수 반환
    else:
        F.append(mfib(n-1, F) + mfib(n-2, F))   # 재귀 호출 후 계산 결과 저장
        return F[n]			        # n번째 피보나치 수 반환

# main program
print(mfib(5))
print(mfib(100))
