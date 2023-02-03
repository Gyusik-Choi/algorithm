N = int(input())
answer = 0
for t in range(N):
    word = input()
    alpha = dict()
    for i in range(len(word)):
        ascii = ord(word[i]) - 97
        if ascii not in alpha:
            alpha[ascii] = [i]
        else:
            alpha[ascii] += [i]

    check = True
    for key, value in alpha.items():
        if len(value) > 1:
            for i in range(len(value) - 1):
                if value[i + 1] - value[i] > 1:
                    check = False
                    break
    if check:
        answer += 1

print(answer)
