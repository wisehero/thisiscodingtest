n = input()
stack = []
answer = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    else:
        if n[i - 1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
