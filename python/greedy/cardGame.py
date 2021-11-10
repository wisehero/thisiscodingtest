# 카드의 행와 열 개수
n, m = map(int, input().split())
# 2차원 리스트
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

max = 0

for i in range(n):
    if max < min(matrix[i]):
        max = min(matrix[i])

print(max)



