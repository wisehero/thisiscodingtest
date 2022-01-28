n, m = map(int, input().split())

no_heard = set()
no_see = set()

for i in range(n + m):
    if i <= n - 1:
        no_heard.add(input())
    elif i >= n + 1:
        no_see.add(input())
    else:
        pass

no_heard_see = list(no_heard.intersection(no_see))
no_heard_see.sort()

print(len(no_heard_see))
for i in no_heard_see:
    print(i)
