n = int(input())
lst = [x for x in range(1, n + 1)]
lst2 = []
stack = []
result = []
for _ in range(n):
    stack.append(int(input()))

# [1,2,3,4,5,6,7...,n]
i = 0
j = 0
while j < len(stack):
    # 스택 대조용 배열의 길이가 0이 아니고 스택의 맨 끝 원소가 스택의 j 번째와 같으면 pop
    if len(lst2) != 0 and lst2[-1] == stack[j]:
        lst2.pop()
        result.append("-")
        j += 1
        continue
    # 만약 1부터 n까지의 요소를 담은 리스트의 크기와 i가 같고 스택 대조용 리스트의 맨 끝 요소가 스택의 j 번째와 같으면 반복문 탈출
    # 스택으로 배열을 만들 수 없음
    if i == len(lst) and lst2[-1] != stack[j]:
        break
    lst2.append(lst[i])
    result.append("+")
    i += 1

if len(lst2) > 0:
    print("NO")
else:
    for i in result:
        print(i)
