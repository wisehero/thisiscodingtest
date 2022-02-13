def solution(color, prices):
    answer = 0
    # 재포장
    repack_list = repack(color)

    # 재포장이 없다는 가정 하의 가격 계산
    for i in color:
        if i[0] == i[1]:
            answer += prices[0]
        else:
            answer += prices[1]

    # 재포장과 재포장이 아닌 것이 섞여 있는 가격

    return min(answer)


def repack(color):
    same = []
    for i in color:
        if i[0] == i[1]:
            same.append(i)
    color_set = set("".join(color))
    for i in color_set:
        if "".join(color).count(i) >= 2:
            same.append(i * 2)
    return same