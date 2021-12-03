# 유효한 팰린드롬 Deque 풀이
import collections


def isPalindrome(s):
    strs = collections.deque

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
