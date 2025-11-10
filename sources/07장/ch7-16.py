class DNode:
    def __init__(self, item=None):
        self.data = item
        self.next = None
        self.prev = None

class LinkedList:                       # 이중 연결리스트
    def __init__(self):
        self.head = DNode(None)		# 헤더 노드 생성
        self.tail = DNode(None)		# 꼬리 노드 생성
        self.head.next = self.tail	# 헤더 노드와 꼬리 노드 연결
        self.tail.prev = self.head
        self.cp = self.tail		# 초기 커서 위치 설정

    def move_left(self):                # 커서 왼쪽 이동
        if self.cp.prev is not self.head:
            self.cp = self.cp.prev

    def move_right(self):   # 커서 오른쪽 이동
        if self.cp is not self.tail:
            self.cp = self.cp.next

    def insert(self, letter):		# 커서 왼쪽에 letter 삽입
        new_node = DNode(letter)
        new_node.next = self.cp
        new_node.prev = self.cp.prev
        self.cp.prev.next = new_node
        self.cp.prev = new_node

    def delete(self):           # 커서 왼쪽 문자 삭제
        if self.cp.prev is not self.head:
            p = self.cp.prev
            p.prev.next = self.cp
            self.cp.prev = p.prev

    def get_text(self):             # 텍스트 반환
        text = []
        p = self.head.next
        while p is not self.tail:
            text.append(p.data)
            p = p.next
        return "".join(text)
        
# main program
text = input()                  # 입력 텍스트
n = int(input())	        # 편집 명령 개수
E = LinkedList()                # 이중 연결리스트 생성
for x in text:                  # 초기 연결리스트 구성, 커서는 맨 끝에 위치
    E.insert(x)

for _ in range(n):              # 편집 작업 수행
    op = input()                # 편집 명령 입력
    if op[0] == 'L':            # 커서 왼쪽 이동
        E.move_left()
    elif op[0] == 'D':          # 커서 오른쪽 이동
        E.move_right()
    elif op[0] == 'B':          # 커서 왼쪽 문자 삭제
        E.delete()
    elif op[0] == 'P':          # 커서 왼쪽에 문자 입력
        E.insert(op.split()[1])

print(E.get_text())             # 편집 결과 출력

