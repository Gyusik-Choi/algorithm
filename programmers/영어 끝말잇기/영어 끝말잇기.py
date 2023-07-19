def solution(n, words):
    turn = 0
    prev = ''
    word_history = dict()

    while turn * n < len(words):
        for i in range(turn * n, turn * n + n):
            cur = words[i]

            if cur in word_history:
                return [i % n + 1, turn + 1]

            if prev and prev[-1] != cur[0]:
                return [i % n + 1, turn + 1]

            prev = cur

            word_history[prev] = True

        turn += 1

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
