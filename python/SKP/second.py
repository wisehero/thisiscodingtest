from collections import deque

deposit = [500, 1000, -300, 200, -400, 100, -100]


def solution(deposit):
    answer = []
    q = deque()
    for i in deposit:
        if i > 0:
            q.append(i)
        else:
            q[-1] += i
            if q[-1] < 0:
                for i in range(len(q) - 1, 0, -1):
                    sub = q[i]
                    q[i - 1] += sub
                    if q[i - 1] > 0:
                        break

    for i in range(len(q)):
        if q[i] > 0:
            answer.append(q[i])
    return answer


print(solution(deposit))
