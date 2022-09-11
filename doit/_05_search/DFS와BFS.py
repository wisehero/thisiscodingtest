from collections import deque

N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

for i in range(N + 1):
    A[i].sort()  # 번호가 작은 노드부터 방문하기 위해 정렬하기


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


visited = [False] * (N + 1)
DFS(Start)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


print()
visited = [False] * (N + 1)
BFS(Start)
