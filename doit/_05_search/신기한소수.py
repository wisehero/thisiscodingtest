import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())


# 소수 판별
def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):  # 소수이면 자릿수 늘림
                DFS(number * 10 + i)


# 일의 자리 소수는 2, 3, 5, 7 이므로 4가지 수에서만 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)
