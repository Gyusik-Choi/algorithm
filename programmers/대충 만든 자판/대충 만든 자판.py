def solution(keymap, targets):
    key_dict = dict()

    for word in keymap:
        for idx, char in enumerate(word):
            if char in key_dict:
                key_dict[char] = min(key_dict[char], idx + 1)
            else:
                key_dict[char] = idx + 1

    result = []

    for target in targets:
        sums = 0

        for idx, t in enumerate(target):
            if t in key_dict:
                sums += key_dict[t]
            else:
                sums = -1
                break

        result.append(sums)

    return result


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
