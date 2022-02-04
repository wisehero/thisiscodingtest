computer = int(input())
pair = int(input())
graph = [[] for _ in range(computer + 1)]
k = 0
while k < pair:
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
    k += 1

visited = [False] * (computer + 1)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

print(visited.count(True) - 1)
