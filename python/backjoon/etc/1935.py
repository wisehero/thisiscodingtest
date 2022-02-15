N = int(input())
sen = input()
alpha = [0] * N

for i in range(N):
    alpha[i] = int(input())

stack = []

for i in sen:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        else:
            stack.append(str1 / str2)

print('%.2f' % stack[0])
