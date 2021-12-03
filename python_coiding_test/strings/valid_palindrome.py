# 유효한 팰린드롬 리스트 풀이

def isPalindrome(self, s) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
