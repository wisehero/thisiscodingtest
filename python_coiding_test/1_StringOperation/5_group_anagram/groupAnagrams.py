import collections

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strlist):
    anagrams = collections.defaultdict(list)

    for word in strlist:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


print(group_anagrams(strings))
