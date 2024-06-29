import re
from collections import Counter


def solution(str1, str2):
    pattern = re.compile('[a-z]{2}')

    str1_lst = [str1[i:i+2].lower() for i in range(len(str1) - 1) if re.findall(pattern, str1[i:i+2].lower())]
    str2_lst = [str2[i:i+2].lower() for i in range(len(str2) - 1) if re.findall(pattern, str2[i:i+2].lower())]

    str1_counter = Counter(str1_lst)
    str2_counter = Counter(str2_lst)

    intersections = sum((str1_counter & str2_counter).values())
    unions = sum((str1_counter | str2_counter).values())

    multiplier = 65536
    return multiplier if not unions else int(intersections / unions * multiplier)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2',	'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('aaa', 'bbb'))  # 0
