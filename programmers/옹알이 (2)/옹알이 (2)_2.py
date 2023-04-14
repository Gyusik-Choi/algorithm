def solution(babbling):
    cnt = 0
    pronounce_list = ["aya", "ye", "woo", "ma"]

    for i, babble in enumerate(babbling):
        for j, pronounce in enumerate(pronounce_list):
            if pronounce * 2 in babble:
                break

            babble = babble.replace(pronounce, '')

        if not babble:
            cnt += 1

    return cnt


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
