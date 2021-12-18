import sys

array = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]
array.sort()
for i in array:
    sys.stdout.write(str(i) + '\n')
