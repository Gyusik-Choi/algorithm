T = int(input())
for t in range(1, T + 1):
    word = input()
    length = len(word)
    mid = len(word) // 2
    ans = True
    for i in range(mid):
        if word[i] == '*' or word[length - i - 1] == '*':
            break
        else:
            if word[i] != word[length - i - 1]:
                ans = False
                break
    if ans:
        print("#{} {}".format(t, "Exist"))
    else:
        print("#{} {}".format(t, "Not exist"))
