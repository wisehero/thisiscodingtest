"""
J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇개나 있을까?
대소문자는 구분한다.
"""


def numJewelsInStones(J, S):
    freqs = {}
    count = 0

    # 돌의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    for char in J:
        if char in freqs:
            count += freqs[char]
