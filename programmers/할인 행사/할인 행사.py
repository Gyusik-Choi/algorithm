def is_all_zero(want_dict):
    for value in want_dict.values():
        if value:
            return False
    return True


def is_discount_possible(want_dict, discount_info):
    for d in discount_info:
        if d in want_dict:
            want_dict[d] -= 1
    return is_all_zero(want_dict)


def get_want_dict(want, number):
    want_dict = dict()
    for idx, w in enumerate(want):
        want_dict[w] = number[idx]
    return want_dict


def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 10 + 1):
        if is_discount_possible(get_want_dict(want, number), discount[i: i + 10]):
            answer += 1
    return answer


print(solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
))

print(solution(
    ["apple"],
    [10],
    ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
))
