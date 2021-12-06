n = int(input())

grade = list(map(int,input().split()))
maximum = max(grade)
for i in range(len(grade)):
    grade[i] = grade[i]/ maximum * 100

print(sum(grade) / len(grade))