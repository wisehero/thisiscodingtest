def fibo(n):
    answer = 0
    idx = 0
    next = 0
    a = [1, 1]

    while(next <= n):
        next = a[idx] + a[idx+1]
        a.append(next)
        idx = idx + 1
        answer = a[-2]

    return answer