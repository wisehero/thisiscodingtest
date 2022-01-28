import math

n = int(input())

number = str(math.factorial(n))
count = 0

for i in range(len(number) - 1, -1, -1):
    if number[i] == "0":
        count += 1
    else:
        break

print(count)
