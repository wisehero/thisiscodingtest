from collections import deque
import sys


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node2].append(node1)
    graph[node1].append(node2)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)
