# 각회의가 겹치지 않아야 한다.
# 회의실을 사용할 수 있는 회의의 최대 개수 구하기
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수 있다.

import sys

# 회의의 수
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

'''
[[1, 4],
 [3, 5],
 [0, 6],
 [5, 7],
 [3, 8],
 [5, 9],
 [6, 10],
 [8, 11],
 [8, 12],
 [2, 13],
 [12, 14]
 ]
'''

li.sort()
x, y = li[0][0], li[0][1]


