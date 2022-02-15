n = int(input())

graph = []
houses = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global house
        house += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


house = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            houses.append(house)
            result += 1
            house = 0

houses.sort()
print(result)
for i in houses:
    print(i)
