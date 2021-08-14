# 한가지 간과한 점은
# 이동거리 테이블을 만들때 문자열의 가운데를 경계로 생각하면 안됐다는 것이다
# 계속 일지하면 가운데를 넘어서 접두사와 접미사가 경계점을 서로 넘어설 수 있는데 그 점을 제대로 생각하지 못했다
def kmp():
    answer = -1
    s_length = len(string)
    p_length = len(pattern)
    idx, distance, cnt = 0, 0, 0
    flag = False

    while True:
        idx = 0
        if idx + distance + p_length > s_length:
            break

        while string[idx + distance] == pattern[cnt]:
            cnt += 1
            idx += 1
            if cnt == p_length:
                answer = distance + 1
                flag = True
                break

        distance = distance + (cnt - distance_table[cnt])
        cnt = 0

    if not flag:
        return answer
    return answer


def create_distance_table(p, p_length):
    table = [0] * (p_length + 1)
    table[0] = -1
    length = 0
    for k in range(1, p_length):
        while p[length] != p[k] and length > 0:
            length = table[length]

        if p[length] == p[k]:
            length += 1
            table[k + 1] = length
    return table


string = "ABAABACABAACCABACABACABAACABACABAAC"
pattern = "ABACABAAC"
# pattern = "ABABABAC"

# 불일치시 이전의 길이의 경계 값을 찾는다.
# 몇칸을 뛰어넘고 다시 경계 값을 찾아야할지 알기 위해서.
# https://bowbowbow.tistory.com/6
# 이 글의 pi 배열 구하는 과정이 이해하는데 많은 도움이 됐다

# ABABAB
# ABABAC
distance_table = create_distance_table(pattern, len(pattern))
print(distance_table)
number = kmp()
print(number)
