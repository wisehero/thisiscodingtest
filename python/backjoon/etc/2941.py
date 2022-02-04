a = set()
a.add("lj")
a.add("c=")
a.add("c-")
a.add("d-")
a.add("nj")
a.add("dz=")
a.add("s=")
a.add("z=")

s = input()
cnt = 0
k = 0

while k < len(s):
    if k < len(s) - 1 and s[k] + s[k + 1] in a:
        cnt += 1
        k += 2
    elif k < len(s) - 2 and s[k:k + 3] in a:
        cnt += 1
        k += 3
    else:
        cnt += 1
        k += 1
print(cnt)
