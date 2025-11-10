"""프로그램 5.1: 괄호를 검사하는 프로그램"""

class Stack:
    """파이썬 리스트를 사용하여 구현한 스택 클래스"""
    def __init__(self):		# 공백 스택을 생성한다.
        self._data = []

    def empty(self):	        # 스택이 공백이면 True, 아니면 False를 반환한다.
        return len(self._data) == 0

    def push(self, item):	# 스택에 원소 item을 삽입한다.
        self._data.append(item)

    def pop(self):		# 스택의 top 원소를 삭제한 후 반환한다.
        if self.empty():
            return None
        return self._data.pop()

    def peek(self):		# 스택의 top 원소를 반환한다.
        if self.empty():
            return None
        return self._data[-1]

def is_valid(text):
    """문자열 text에서 괄호 사용이 유효하면 True, 아니면 False를 반환한다."""
    S = Stack()		                        # 공백 스택 생성
    for ch in text:
        if ch in ['(', '{', '[']: 	        # 왼쪽 괄호면 스택에 삽입
            S.push(ch)
        elif ch in [')', '}', ']']:	        # 오른쪽 괄호인 경우
            if S.empty():		        # 왼쪽 괄호가 부족한 경우
                return False
            chs = S.pop()		        # 스택의 top 괄호 삭제
            # 괄호 짝 검사
            if (ch== ')' and chs != '(') or \
               (ch== '}' and chs != '{') or \
               (ch== ']' and chs != '['):
                return False
    return S.empty()			# 마지막에 스택이 공백이어야 함

# main program
text = "A * [ { ( B + C ) / D } - E ] + F"
if is_valid(text):
    print('VALID')
else:
    print('WRONG')

text = "[ A ( B ) } C { ]"
if is_valid(text):
    print('VALID')
else:
    print('WRONG')
