from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    dic = defaultdict(list)

    for idx, s in enumerate(strs):
        sorted_s = ''.join(sorted(s))
        dic[sorted_s].append(s)

    return list(dic.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

