"""
숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []
"""


def combinationSum(candidates, target):
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))

