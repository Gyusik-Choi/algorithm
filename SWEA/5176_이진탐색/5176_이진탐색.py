def make_tree(n):
    global cnt
    if n <= N:
        make_tree(n * 2)
        arr[n] = cnt
        cnt += 1
        make_tree(n * 2 + 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cnt = 1
    arr = [0] * (N + 1)
    make_tree(1)
    print("#{} {} {}".format(t, arr[1], arr[N // 2]))

# 참고
# https://mungto.tistory.com/209
