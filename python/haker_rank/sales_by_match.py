def sockMerchant(n, ar):
    # Write your code here
    pair = 0
    ar_set = set(ar)
    for i in ar_set:
        pair += ar.count(i) // 2
    return pair
