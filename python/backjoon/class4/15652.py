from itertools import product

n, m = map(int, input().split())
numbers = list(x for x in range(1, n + 1))
product_result = list(product(numbers, repeat=m))

if m > 1:
    for i in product_result:
        if max(i) == i:
            continue
        else:
            for j in i:
                print(j, end=" ")
            print()


else:
    for i in product_result:
        for j in i:
            print(j, end=" ")
        print()
