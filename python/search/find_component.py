import sys


# 실전문제 이진탐색 풀이

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 반환
        if array[mid] == target:
            return mid
        # 중간 점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간 점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        return None


n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip()))
n_list.sort()

m = int, sys.stdin.readline().rstrip()
m_list = list(map(int, sys.stdin.readline().rstrip()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in m_list:
    # 해당 부품이 존재하는지 확인
    result = binary_search(n_list, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
