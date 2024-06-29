import math
import re


def solution(str1, str2):
    pattern = re.compile('[a-zA-Z]')
    multiplier = 65536

    str1_lst = list(map(lambda s: s.lower(), str1))
    str2_lst = list(map(lambda s: s.lower(), str2))

    split_str1 = []
    for i in range(len(str1_lst) - 1):
        word = ''.join(str1_lst[i:i + 2])
        if word == ''.join(re.findall(pattern, word)):
            split_str1.append(word)

    split_str2 = []
    for i in range(len(str2_lst) - 1):
        word = ''.join(str2_lst[i:i + 2])
        if word == ''.join(re.findall(pattern, word)):
            split_str2.append(word)

    str1_dict = dict()
    str2_dict = dict()

    for word in split_str1:
        if word in str1_dict:
            str1_dict[word] += 1
        else:
            str1_dict[word] = 1

    for word in split_str2:
        if word in str2_dict:
            str2_dict[word] += 1
        else:
            str2_dict[word] = 1

    intersections = 0
    unions = 0

    for k, v in str1_dict.items():
        if k in str2_dict:
            intersections += min(v, str2_dict[k])
            unions += max(v, str2_dict[k])
        else:
            unions += v

    for k, v in str2_dict.items():
        if k not in str1_dict:
            unions += v

    if not unions:
        return multiplier
    return math.floor(intersections / unions * multiplier)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2',	'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('aaa', 'bbb'))  # 0
