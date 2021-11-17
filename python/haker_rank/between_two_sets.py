from math import gcd


# 리스트의 최대 공약수
def gcd_list(nums):
    gcd_nums = None
    for i in range(len(nums)):
        if i == 0:
            gcd_nums = nums[i]
        else:
            gcd_nums = gcd(gcd_nums, nums[i])
    return gcd_nums


# 최소 공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


# 리스트의 최소 공배수
def lcm_list(nums):
    lcm_nums = None
    for i in range(len(nums)):
        if i == 0:
            lcm_nums = nums[i]
        else:
            lcm_nums = lcm(lcm_nums, nums[i])
    return lcm_nums


def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)

    # a의 공배수들 중 min_b 이하
    a_cms = []
    i = 1
    while True:
        temp = lcm_a * i
        if temp > gcd_b:
            break

        a_cms.append(temp)
        i += 1

    answer = 0
    for temp in a_cms:
        is_factor = True
        for bb in b:
            if bb % temp != 0:
                is_factor = False
            if is_factor:
                answer += 1
    return answer
