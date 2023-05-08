from collections import defaultdict
import re


def most_common_word(paragraph, banned):
    p = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
    dic = defaultdict(int)

    for idx, word in enumerate(p):
        if word not in banned:
            dic[word] += 1

    most_common = ''
    max_cnt = 0

    for key, value in dic.items():
        if max_cnt < value:
            max_cnt = value
            most_common = key

    return most_common


print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
