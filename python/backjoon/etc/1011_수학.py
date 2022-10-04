# 구글링한 문제
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0  # 이동횟수
    move = 1  # count 별 빈도 수
    move_plus = 0  # 이동한 거리 합
    while move_plus < distance:
        count += 1
        move_plus += move
        if count % 2 == 0:
            move += 1
    print(count)
