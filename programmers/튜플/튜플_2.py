import re
from collections import Counter


def solution(s):
    return list(map(lambda x: x[0], sorted(Counter(list(map(int, re.findall(r"\d+", s)))).items(), key=lambda x: x[1], reverse=True)))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
