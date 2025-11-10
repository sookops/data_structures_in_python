"""프로그램 9.7: 후위 수식으로부터 수식 트리를 구축하는 프로그램"""

class BinNode:
    def __init__(self, item=None, left_child=None, right_child=None):
        self.data = item	    # 자료 원소
        self.left = left_child	    # 왼쪽 자식을 가리키는 링크
        self.right = right_child    # 오른쪽 자식을 가리키는 링크

def make_expr_tree(postfix):        # postfix : 후위 수식의 토큰 리스트
    if not postfix:                         # 빈 수식인 경우 None 반환
        return None	
    stack = []			            # 리스트를 이용한 스택 표현
    for token in postfix: 	            # 각 연산자 또는 피연산자에 대해
        p = BinNode(token)	            # 트리 노드 생성
        if token in ['+', '-', '*', '/']:   # token이 연산자이면
            p.right = stack.pop()	    # 오른쪽 자식으로 연결
            p.left = stack.pop()	    # 왼쪽 자식으로 연결
        stack.append(p)	                    # 스택에 트리 노드 삽입
    return stack[0]			    # 루트 노드 반환

def evaluate(p):
    if p is None: 		            # 빈 수식이면 None 반환
        return None
    if p.left is None and p.right is None:  # 잎 노드이면
        return p.data	    	            # 피연산자 반환
    lval = evaluate(p.left)		    # 왼쪽 부트리 계산
    rval = evaluate(p.right)	            # 오른쪽 부트리 계산
    return str(eval(lval + p.data + rval))  # 계산 결과를 문자열로 반환

def get_prefix(p):		# 전위 수식 생성
    if p is None: 	        # 공백 리스트 반환
        return []
    L = get_prefix(p.left)	# 왼쪽 부트리로부터 전위 수식 생성
    R = get_prefix(p.right)	# 오른쪽 부트리로부터 전위 수식 생성
    return [p.data] + L + R	# 전위 수식 반환

def get_postfix(p):		# 후위 수식 생성
    if p is None:       	# 공백 리스트 반환
        return []
    L = get_postfix(p.left)	# 왼쪽 부트리로부터 후위 수식 생성
    R = get_postfix(p.right)	# 오른쪽 부트리로부터 후위 수식 생성
    return L + R + [p.data]	# 후위 수식 반환

def get_infix(p):		# 중위 수식 생성
    if p is None:               # 공백 리스트 반환
        return [] 
    if p.left is None and p.right is None:
        return [p.data]		# 잎 노드인 피연산자에는 괄호 없이 반환
    L = get_infix(p.left)	# 왼쪽 부트리로부터 중위 수식 생성
    R = get_infix(p.right)	# 오른쪽 부트리로부터 중위 수식 생성
    return ['('] + L + [p.data] + R + [')']	# 중위 수식 반환
    
# main program
expr = "6 4 2 - 3 * +"                  # 6 + ((4 - 2) * 3)
root = make_expr_tree(expr.split())     # 수식 트리 생성 - 프로그램 9.7
print(*get_prefix(root)) 		# 출력 결과 : + 6 * - 4 2 3
print(*get_postfix(root))		# 출력 결과 : 6 4 2 - 3 * +
print(*get_infix(root))			# 출력 결과 : ( 6 + ( ( 4 - 2 ) * 3 ) )

