# 문자열 탐색 알고리즘
# 접두사, 경계, 접미사
# 탐색을 하기 전에 패턴의 길이별 최대 경계 길이를 구하는 테이블을 만들어둔다


def kmp():
    pass


# 인덱스별로 따로 구하지 않고 다음 인덱스 값을 구할때 이전 인덱스값을 활용한다
def create_distance_table(p, p_length):
    table = [0] * (p_length + 1)
    return table


string = "ABAABACABAACCABACABACABAACABACABAAC"
pattern = "ABACABAAC"

distance_table = create_distance_table(pattern, len(pattern))
kmp()

# https://chanhuiseok.github.io/posts/algo-14/
# https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
