from collections import Counter

# 리스트의 요소 개수 세기
L = [1, 4, 5, 5, 2, 1, 5, 2, 5, 2]
freq = Counter(L)
print(freq[3])              # 존재하지 않은 키 3에 대한 검색, 0 출력
freq.update([1, 1, 1])      # [1, 1, 1]을 추가하여 개수를 셈
print(freq.most_common(2))  # 상위 2개의 요소와 빈도수 출력
# 출력 : [(1, 5), (5, 4)]
print(freq.most_common())   # 모든 요소를 빈도수 순으로 나열
# 출력 : [(1, 5), (5, 4), (2, 3), (4, 1)]

# 문자열의 문자 개수 세기
C1 = Counter("hello")       
C2 = Counter("world")      
print(C1)       # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
print(C2)       # Counter({'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1})

print(C1+C2)    # 덧셈 (요소 개수를 더함)
# 출력 : Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
print(C1-C2)    # 뺄셈 (0보다 작으면 포함하지 않음)
# 출력 : Counter({'h': 1, 'e': 1, 'l': 1})

