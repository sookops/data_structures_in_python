"""프로그램 5.2: 후위 수식을 계산하는 프로그램"""

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

def eval_postfix(E):
    """후위 수식 E의 계산 결과를 반환한다."""
    S = Stack()		                # 공백 스택 생성
    tokens = E.split()	                # 토큰들의 리스트 구성
    for tk in tokens:	                # 각 토큰에 대해서 수행
        if tk.isdigit(): 	        # 숫자인 경우 스택에 삽입
            S.push(int(tk))
        else:		                # 연산자인 경우
            y = S.pop()		        # 오른쪽 피연산자
            x = S.pop() 	        # 왼쪽 피연산자
            if tk == '+': S.push(x+y)	# 계산 결과를 스택에 삽입
            elif tk == '-': S.push(x-y)
            elif tk == '*': S.push(x*y)
            elif tk == '/': S.push(x//y)
    return S.peek()		        # 최종 계산 결과 반환						# 최종 계산 결과 반환

# main program
print(eval_postfix('2 3 * 4 +'))
print(eval_postfix('3 8 2 / 5 3 - * +'))
