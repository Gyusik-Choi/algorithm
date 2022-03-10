import sys


def combination(num1, num2, idx1, idx2):
    whole_idx = idx2 - idx1 + 1

    whole_sums = 0
    for i in range(idx1, idx2 + 1):
        whole_sums += weights_dict[list_weights_dict[i]]

    # {1: 1, 2: 1, 3: 1} 의 경우를 계산하려 했으나
    # 3 C 3, 3 C 2 의 경우만 구해야하고
    # 3 C 1, 3 C 0 은 구하면 안 된다
    # 점점 꼬여간다

    # 또한 이전에 구했던 것을 또 구하게 되거나
    # 혹은 제대로 못구하게 되는 경우가 나올 수 있어서
    # 이 방법으로는 힘들 듯 하다
    # 예를들어
    # 5 6
    # 1 2 3 4 5
    # 딕셔너리로 갯수를 세면 아래와 같이 된다
    # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    # 1, 2, 3이 6이니까 이때의 경우를 구하고
    # 2 3도 6보다 작아서 가능한 경우라 경우를 구하게 되면
    # 중복해서 구하게 된다

    # {1: 3, 2: 2, 3: 4}
    # whole_sums C whole_idx
    # until whole_idx > 1
    ways = 0
    while whole_idx > 1:
        # 분자
        numerator = 1
        whole_num_multiplication = whole_sums
        for _ in range(whole_idx):
            numerator *= whole_num_multiplication
            whole_num_multiplication -= 1

        # 분모
        denominator = 1
        whole_idx_multiplication = whole_idx
        for _ in range(whole_idx):
            denominator *= whole_idx_multiplication
            whole_idx_multiplication -= 1

        ways += numerator // denominator
        whole_idx -= 1

    return ways


def sliding_window():
    start = 0
    end = 0
    ways = 0
    sums = list_weights_dict[start]

    while start <= end < len(list_weights_dict):
        if sums <= C:
            if start < end:
                # 4 6
                # 1 5 3 2
                # => 10
                # 여기서 1 2 이후에 1 2 3 도 되는데
                # 기존의 방법으로는 2 3 의 경우를 제대로 계산하지 못한다
                # 중복되거나 아니면 아예 누락이 된다

                # 이를 개선하기 위해 아예 최대한의 범위로 end 를 이동시킨 후 계산( 2 ** x - 1)
                if end + 1 < len(list_weights_dict):
                    if sums + list_weights_dict[end + 1] < C:
                        end += 1
                        sums += list_weights_dict[end]
                    else:
                        ways += combination(list_weights_dict[start], list_weights_dict[end], start, end)
                        end += 1
                        sums += list_weights_dict[end]
                else:
                    break
            else:
                end += 1
                sums += list_weights_dict[end]
        else:
            sums -= list_weights_dict[start]
            start += 1

    # 각 요소별 갯수를 구한다
    for key, value in weights_dict.items():
        ways += 2 ** value - 1

    return ways + 1


# 물건수, 최대 무게
N, C = map(int, sys.stdin.readline().split())
# 물건 무게
weights = list(map(int, sys.stdin.readline().split()))

if C != 0:
    weights.sort()
    weights_dict = {}
    for weight in weights:
        if weight not in weights_dict:
            weights_dict[weight] = 1
        else:
            weights_dict[weight] += 1

    list_weights_dict = list(weights_dict)
    if list_weights_dict[0] > C:
        print(1)
    elif len(list_weights_dict) == 1 and C == list_weights_dict[0]:
        print(2 ** weights_dict[list_weights_dict[0]])
    else:
        print(sliding_window())
else:
    print(1)

# https://velog.io/@flaxinger/ALGO-Meet-In-The-Middle
# https://www.adamsmith.haus/python/answers/how-to-access-a-dictionary-key-by-index-in-python

# 3 3
# 1 1 1
# [], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]
# 3C0 부터 3C3 까지 모두 구하는 것인데 이는 2 ** 3 과 같다

# 4 4
# 1 2 3 4
# [], [0], [1], [2], [3], [0, 1]

# 4 4
# 1 1 2 2
# {1: 2, 2: 2}
# [], [0], [1], [2], [3], [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3] ...
# 개별 조합은 -1을 해줘야 한다
# 1이 2개인데 이거 2개를 조합하면 총 4개이나 공백도 포함이 돼서
# 이는 2에서도 조합의 경우로 나오므로 여기서도 1을 빼주고
# 공백에 대한건 최종적으로 더해주면 된다

# C 밑으로만 해서
# 딕셔너리로 각 요소별 갯수를 구한다
# 각 요소별 조합은 미리 구하고 (여기 조합은 2 ** 요소 갯수 - 1)
# 슬라이딩 윈도우로 2개 이상의 경우로만 조합을 구한다
# 조합은 조합 공식을 직접 for 문으로 곱해주고 나누는 방식으로

# 반례
# 2 1
# 1 1
# => 3

# 2 1
# 2 2
# => 1

# 4 4
# 1 2 3 4
# => 7

