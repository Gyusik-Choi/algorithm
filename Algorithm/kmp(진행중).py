# 문자열 탐색 알고리즘
# 접두사, 경계, 접미사
# 탐색을 하기 전에 패턴의 길이별 최대 경계 길이를 구하는 테이블을 만들어둔다


def kmp():
    answer = -1
    s_length = len(string)
    p_length = len(pattern)
    distance, idx, cnt = 0, 0, 0
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


# 인덱스별로 따로 구하지 않고 다음 인덱스 값을 구할때 이전 인덱스값을 활용한다
def create_distance_table(p, p_length):
    table = [0] * (p_length + 1)
    table[0] = -1
    j = 0
    for k in range(1, p_length):
        while p[j] != p[k] and j > 0:
            j = table[j]

        if p[j] == p[k]:
            j += 1
            table[k + 1] = j
    return table

    # table = [0] * (p_length + 1)
    # table[0] = -1
    # idx = 2
    # length = 0
    # # 마지막 인덱스는 0으로 두기 위해 while 문의 범위에 포함되지 않도록 조정
    # while idx < p_length:
    #     if p[idx - 1] == p[length]:
    #         idx += 1
    #         length += 1
    #         table[idx - 1] = length
    #     else:
    #         if length == 0:
    #             table[idx] = 0
    #             idx += 1
    #         else:
    #             # length -= 1 <- 이건 왜 안되는지 이해 필요
    #             length = table[length - 1]
    # return table


string = "ABAABACABAACCABACABACABAACABACABAAC"
pattern = "ABACABAAC"

distance_table = create_distance_table(pattern, len(pattern))

number = kmp()
print(number)

# 참고
# https://chanhuiseok.github.io/posts/algo-14/
# https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
