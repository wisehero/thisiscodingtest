a = 300
b = 60
c = 10
countA = 0
countB = 0
countC = 0
fail = -1
t = int(input())

while t != 0:
    if t >= a:
        countA += t // a
        t = t % a

    if t >= b:
        countB = t // b
        t = t % b

    if t >= c:
        countC = t // c
        t = t % c
    if t % a != 0:
        print(fail)
        exit()

print(countA, countB, countC)
