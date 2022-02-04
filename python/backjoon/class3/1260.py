from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

dfs_graph = [[] for _ in range(n + 1)]
bfs_graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

counter = 0

while counter < m:
    x, y = map(int, input().split())
    dfs_graph[x].append(y)
    dfs_graph[y].append(x)
    bfs_graph[x].append(y)
    bfs_graph[y].append(x)
    counter += 1

dfs(dfs_graph, v, dfs_visited)
print()
bfs(bfs_graph, v, bfs_visited)
