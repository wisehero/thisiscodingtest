def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    strs = []
    for char in s:
        if char.isalnum():  # isalnum() : 영문자와 숫자 판별
            strs.append(char.lower())  # lower() 소문자로 변경
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True
