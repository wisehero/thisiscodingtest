s = input()

s_list = s.strip(" ").split(" ")
count = 0
for i in s_list:
    if i != "":
        count += 1
print(count)
