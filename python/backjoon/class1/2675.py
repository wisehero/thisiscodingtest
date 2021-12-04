t = int(input())  # 테스트 케이스 개수 입력받기

for i in range(t):
    a, b = input().split()
    a, b = int(a), list(b)
    for j in b:
        print(j * a, end='')
    print()
