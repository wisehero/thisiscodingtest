# 각 문자열이 등장한 횟수 만큼 딕셔너리에 저장한다.
# 각 문자열을 키에 매핑된 밸류를 전부 비교했을 때 전부 다 같아야 한다.
# 같지 않은 키의 밸류를 제거하는 건 한번만 가능하다.
# 밸류안에 1이 있으면 완전히 제거해야한다.
# 1보다 크면 1개를 줄이는 시도를 한다.
from collections import Counter
def isValid(s):
    d = Counter(Counter(s).values())
    if len(d) == 1:
        return "YES"
    if len(d) > 2:
        return "NO"
    if 1 in d.values() and (d[min(d.keys())] == 1 or (max(d.keys()) - min(d.keys()) == 1)):
        return "YES"
    else:
        return "NO"





