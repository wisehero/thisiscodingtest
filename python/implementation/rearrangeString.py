s = input()
alpha_list = []
number = 0
for i in s:
    if i.isalpha():
        alpha_list.append(i)
    else:
        number += int(i)

alpha_list.sort()
print("".join(alpha_list) + str(number))

