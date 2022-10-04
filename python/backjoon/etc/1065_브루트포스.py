n = int(input())
count = 0
for i in range(1, n + 1):
    if i < 10:
        count += 1
    elif i < 100:
        count += 1
    elif i < 1000:
        num_list = list(map(int, str(i)))
        if (num_list[0] + num_list[2]) / 2 == float(num_list[1]):
            count += 1

print(count)
