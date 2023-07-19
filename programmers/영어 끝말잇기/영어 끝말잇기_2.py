def solution(n, words):
    prev = words[0]
    word_history = dict()
    word_history[prev] = True

    for i in range(1, len(words)):
        cur = words[i]

        if cur in word_history or prev[-1] != cur[0]:
            return [i % n + 1, i // n + 1]

        prev = cur
        word_history[prev] = True

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
