def breakingRecords(scores):
    min, max, minimum, maximum = 0, 0, 0, 0
    for i in range(len(scores)):
        if i==0:
            minimum = scores[i]
            maximum = scores[i]
            continue
        if scores[i] > maximum:
            maximum = scores[i]
            max += 1
        if scores[i] < minimum:
            minimum = scores[i]
            min += 1
    return max, min

scores = [10,5,20,20,4,5,2,25,1]
print(breakingRecords(scores))
