"""프로그램 4.6: 회문 여부를 판별하는 재귀 함수"""

def palindrome(str, low, high):
    """str[low:high+1]이 회문이면 True, 아니면 False를 반환하는 재귀 함수"""
    if low >= high: 		# 종료 조건 - 문자가 없거나 하나만 있으면
        return True		# 회문으로 판정
    if str[low] != str[high]:	# 양 끝 문자가 다르면
        return False		# 회문이 아닌 것으로 판정
    return palindrome(str, low+1, high-1)   # 양 끝을 뺀 부문자열 검사

# main program
text = "nursesrun"
print(palindrome(text, 0, len(text)-1))

text = "wasitacatisaw"
print(palindrome(text, 0, len(text)-1))

text = "helloh"
print(palindrome(text, 0, len(text)-1))
