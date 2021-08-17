def kmp():
    answer = -1
    string_length = len(string)
    pattern_length = len(pattern)
    distance_table = create_distance_table(pattern, pattern_length)
    idx, distance, cnt = 0, 0, 0
    while True:
        idx = 0
        if idx + distance + pattern_length > string_length:
            break

        while string[idx + distance] == pattern[cnt]:
            idx += 1
            cnt += 1
            if cnt == pattern_length:
                answer = distance + 1
                break

        distance = distance + (cnt - distance_table[cnt])
        cnt = 0

    return answer


def create_distance_table(p, p_length):
    table = [0] * (p_length + 1)
    table[0] = -1
    length = 0
    for i in range(2, p_length):
        while p[length] != p[i] and length > 0:
            length = table[length]

        if p[length] == p[i]:
            length += 1
            table[i + 1] = length
    return table


string = "ABAABACABAACCABACABACABAACABACABAAC"
pattern = "ABACABAAC"
ans = kmp()
print(ans)
