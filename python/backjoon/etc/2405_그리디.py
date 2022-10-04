import sys


def calculate(a, b, c):
    return abs(a + b + c - 3 * b)


n = int(sys.stdin.readline())
number_list = [int(sys.stdin.readline()) for _ in range(n)]

number_list.sort()

answer = - 1
for i in range(1, n - 1):
    answer = max(answer, calculate(number_list[i - 1], number_list[i], number_list[n - 1]))
    answer = max(answer, calculate(number_list[0], number_list[i], number_list[i + 1]))

print(answer)
