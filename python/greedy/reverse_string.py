s = input()

# 문자열에 0이 많은지 1이 많은지 비교하여 선택
# 더 많은 쪽이 연속으로 몇번 나타나는 지 카운트

if s.count("0") < s.count("1"):
    choice = "1"
else:
    choice = "0"

s_list = s.split(choice)
print(s_list)
result = len(s_list) - s_list.count('')
print(result)
