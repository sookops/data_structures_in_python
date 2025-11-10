"""프로그램 7.9: 원형 연결리스트를 이용하여 요셉 문제를 해결하는 프로그램"""

class Node:
    def __init__(self, item=None, link=None):
        self.data = item	    # 자료 원소 저장
        self.next = link	    # 링크 저장

def josephus(n, k):
    """요셉 문제를 해결하는 프로그램:
    n명으로 시작하여 k번째 사람을 반복적으로 제거할 때 최후로 살아남을 수 있는 
    위치를 반환한다."""  
    head = Node(1)		    # 시작 노드 생성
    head.next = head	            # 초기 원형 연결리스트
    tail = head		            # 끝 노드를 가리키는 변수

    for i in range(2, n+1):	    # n개 노드의 원형 연결리스트 구성
        p = Node(i, head)           # 시작 노드를 가리키는 새 노드 생성
        tail.next = p	            # 현재 끝 노드가 새 노드를 가리킴
        tail = p	            # tail이 새 끝 노드를 가리킴

    # 시뮬레이션 수행
    while n > 1:		    # 마지막 한 명이 남을 때까지 반복
        for _ in range((k-1) % n):  # k-1 번째 노드로 이동
            p = p.next
        p.next = p.next.next	    # k번째 노드 삭제
        n -= 1			    # 노드 수 1 감소

    return p.data		    # 최후의 생존자 위치 반환

# main program
n, k = [int(x) for x in input().split()]
print(josephus(n, k))

'''
from collections import deque 


def josephus_queue(n, k):
    Q = deque()
    for i in range(1, n+1):	    # 1부터 n까지 큐에 삽입
        Q.append(i)
    while n > 1:		    # 마지막 한 명이 남을 때까지 반복
        for j in range((k-1) % n):  # k-1번째 위치까지는 큐에 다시 삽입
            Q.append(Q.popleft())
        Q.popleft()
        n -= 1	                    # k번째 위치 제거								# 큐에 저장된 원소 개수 감소
    return Q[0]			    # 최후의 생존자 위치

print(josephus_queue(n, k))
'''
