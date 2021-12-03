import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(group_anagrams(strs))
