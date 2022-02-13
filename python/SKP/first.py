t = [3, 5, 2, 9, 8]
m = 3


def solution(t, m):
    answer = 0
    t.sort()
    for i in range(m):
        t[i] += 1
        answer += t[i]
    return answer


print(solution(t, m))
