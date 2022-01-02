n = input()
left = n[:len(n)//2]
right = n[len(n)//2:]

left = list(map(int, left))
right = list(map(int, right))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
