from collections import Counter


def solution(s):
    return list(map(lambda x: x[0], sorted(Counter(list(map(int, ''.join(''.join(s.split('{')).split('}')).split(',')))).items(), key=lambda x: x[1], reverse=True)))


# 위의 한 줄 코드를 아래와 같이 풀어서 표현할 수 있다
def solution2(s):
    s1 = ''.join(s.split('{'))
    s2 = ''.join(s1.split('}'))
    s3 = s2.split(',')
    lst = list(map(int, s3))
    counter = Counter(lst)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], sorted_counter))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
