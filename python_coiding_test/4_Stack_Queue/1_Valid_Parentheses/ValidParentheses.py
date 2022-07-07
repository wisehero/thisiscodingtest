"""
괄호로 된 입력값이 올바른지 판별하라

입력 : ()[]{}
출력 : true
"""
s = '()[]{}'


def isValid(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 스택 이용 예외처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


isValid(s)
