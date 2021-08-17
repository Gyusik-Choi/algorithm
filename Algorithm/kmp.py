# 한가지 간과한 점은
# 이동거리 테이블을 만들때 문자열의 가운데를 경계로 생각하면 안됐다는 것이다
# 계속 일지하면 가운데를 넘어서 접두사와 접미사가 경계점을 서로 넘어설 수 있는데 그 점을 제대로 생각하지 못했다

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


# 인덱스별로 따로 구하지 않고 다음 인덱스 값을 구할때 이전 인덱스값을 활용한다.
# 불일치시 이전의 길이의 경계 값을 찾는다.
# 몇칸을 뛰어넘고 다시 경계 값을 찾아야할지 알기 위해서.
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

# 참고
# https://bowbowbow.tistory.com/6
# https://chanhuiseok.github.io/posts/algo-14/
# https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
