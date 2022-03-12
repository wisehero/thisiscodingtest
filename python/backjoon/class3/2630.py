import sys

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

blue = 0
white = 0


def solution(x, y, n):
    global white, blue
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != graph[i][j]:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, n)
print(white)
print(blue)
