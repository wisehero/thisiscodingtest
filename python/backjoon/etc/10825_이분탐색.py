t = int(input())

class_room = []

for _ in range(t):
    arr = list(input().split())
    class_room.append(arr)

class_room.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))  # 국어 점수 오름차순

for i in class_room:
    print(i[0])
