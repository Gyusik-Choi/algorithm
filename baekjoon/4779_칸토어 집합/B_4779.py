def split_strs(strs: list[str]):
    if len(strs) == 1:
        return ''.join(strs)

    mid = ""
    idx = len(strs) // 3
    for i in range(idx, idx + idx):
        strs[i] = " "
        mid += strs[i]

    front = split_strs(strs[:idx])
    back = split_strs(strs[idx + idx:])
    return front + ''.join(list(mid)) + back


while True:
    try:
        n = int(input())
        print(split_strs(list("-" * (3 ** n))))
    except EOFError:
        break
