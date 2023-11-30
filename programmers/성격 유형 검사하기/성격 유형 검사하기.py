from collections import defaultdict


def solution(survey, choices):
    character_info = ["RT", "CF", "JM", "AN"]
    character_point = defaultdict(int)

    for idx, s in enumerate(survey):
        first, second = s[0], s[1]
        choice = choices[idx]

        if choice < 4:
            character_point[first] += 4 - choice
        elif choice > 4:
            character_point[second] += choice - 4

    character = ''

    for info in character_info:
        first_point, second_point = character_point[info[0]], character_point[info[1]]

        if first_point >= second_point:
            character += info[0]
        else:
            character += info[1]

    return character


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
