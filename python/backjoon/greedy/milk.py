'''
처음엔 딸기 우유 마신다.
딸기 우유 다음엔 초코우유
초코우유 다음에 바나나
바나나 다음에 딸기

가게는 딸기 초코 바나나 중에 한 종류 우유만 취급

n = 5

0 1 2 0 1

1 1 0 2 1

0 1 2 0 1
'''
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, input().split()))
max = 0

for i in range(n):
    if (nlist[i] == max % 3):
        max += 1
print(max)





