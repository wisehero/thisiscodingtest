# s-t 사이에 떨어져 있는 사과와 오렌지 갯수를 출력해야 함
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0
    for i in range(len(apples)):
        apples[i] = apples[i] + a
    for j in range(len(oranges)):
        oranges[j] = oranges[j] + b

    for i in range(len(apples)):
        if s <= apples[i] <= t:
            count_apple += 1
    for j in range(len(oranges)):
        if s <= oranges[i] <= t:
            count_orange += 1
    print(count_apple)
    print(count_orange)
