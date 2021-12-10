def solution(arr, x):
    a = []
    re_arr = arr.copy()
    i = 0
    while i < len(arr):  # 배열 끝까지 반복한다
        mex = 0
        arr[i] -= x
        # arr[i]가 0하고 같거나 작아지는 경우
        if arr[i] <= 0:
            # 세트로 바꾼다.
            new_set = set(arr)
            for k in new_set:
                # 만약 mex가 i보다 크거나 같고 i가 0일 경우
                if mex not in new_set:
                    a.append(mex)
                    i += 1
                    break
                elif mex in new_set:
                    mex += 1
            arr = re_arr
            print(arr)
            i += 1
        # arr[i]가 0보다 큰 경우에는 계속해서 빼준다.
        else:
            continue
        print(a)
    return max(a)

arr = [1,3,4]
x = 2
c = solution(arr, 2)
print(c)