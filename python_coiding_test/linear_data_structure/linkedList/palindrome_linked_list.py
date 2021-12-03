# 연결 리스트가 팰린드롬 구조인지 판별하라
# 입력 1->2
# 출력 false
# 입력 1->2->2->1
# 출력 true
import collections


def is_palindrome(head):
    q = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

# 데크 활용 풀이
def is_palindromeV2(head):
    q = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True
