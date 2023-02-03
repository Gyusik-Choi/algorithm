def recursion(cnt):
    if cnt == 10:
        pass
    else:
        cnt = recursion(cnt + 1)
    return cnt


answer = recursion(1)
print(answer)
