import sys


def combination(num1, num2, idx1, idx2):
    # num1과 num2의 갯수 C num2와 num1의 사이에 놓인 갯수
    # num2와 num1의 사이에 놓인 갯수는 list_weights_dict 의 인덱스로 구해야 한다
    whole_num = weights_dict[num1] + weights_dict[num2]
    whole_idx = idx2 - idx1 + 1
    if whole_num == whole_idx:
        return 2 ** whole_idx - 1
    # 분자
    numerator = 1
    whole_num_multiplication = whole_num
    for _ in range(whole_idx):
        numerator *= whole_num_multiplication
        whole_num_multiplication -= 1

    # 분모
    denominator = 1
    whole_idx_multiplication = whole_idx
    for _ in range(whole_idx):
        denominator *= whole_idx_multiplication
        whole_idx_multiplication -= 1

    combinations = numerator // denominator
    return combinations


def sliding_window():
    start = 0
    end = 0
    ways = 0
    sums = list_weights_dict[start]

    while start <= end < len(list_weights_dict):
        if sums <= C:
            if start < end:
                print(start, end, sums)
                way = combination(list_weights_dict[start], list_weights_dict[end], start, end)
                print(way)
                ways += way

            if end + 1 < len(list_weights_dict):
                end += 1
                sums += list_weights_dict[end]
            else:
                break
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
        print(2 ** weights_dict[list_weights_dict[0]] - 1)
    else:
        print(weights_dict)
        print(list_weights_dict)
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
# => 6

# 4 6
# 1 5 3 2
# 정렬하면 (1 2 3 5)
# => 10
# [], [0], [1], [2], [3], [0, 1], [0, 2], [
