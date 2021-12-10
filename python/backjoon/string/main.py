'''
연속된 k는 높은 수익성을 보장한다. 만약 스톡 가격이 몇달간 오른다면
n개의 월이 주어진다.

'''


def solution(stockPrices, k):
    a = 0
    answer = 0
    # 스톡프라이즈 배열이 들어왔을 때 요소 하나하나를 검사
    for i in range(len(stockPrices) - 1):
        if stockPrices[i + 1] > stockPrices[i]:
            a += 1
            if a == k-1:
                answer += 1
                a = 0
        elif stockPrices[i+1] <= stockPrices[i]:
            a = 0
    return answer


print(solution([1,1,1,1,1,1,1], 3))
