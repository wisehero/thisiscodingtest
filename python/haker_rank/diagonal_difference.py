import os

def diagonalDifference(arr):
    a = 0
    b = 0
    for i in range(len(arr)):
        a += arr[i][len(arr) - 1 - i]
    for k in range(len(arr)):
        b += arr[k][len(arr) - n + k]
    return abs(a - b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()