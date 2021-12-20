'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴해라

nums = [2, 7, 11, 15] target = 9

출력 -> [0, 1]
'''


# 브루트 포스
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSumV2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        # 컴플리먼트가 nums[i+1] 배열안에 존재하면 n의 인덱스와 컴플리먼트의 인덱스를 리턴
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 첫 번째 수를 뺀 결과 키 조회
def twoSumV3(nums, target):
    nums_map = {}  # {2: 0, 7: 1, 11: 2, 15: 3}
    # 키와 값을 바궈서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# V3 개선
def twoSumV4(nums, target):
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투 포인터 사용
def twoSumTwoPointer(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


print(twoSumV3([2, 7, 11, 15], 9))
