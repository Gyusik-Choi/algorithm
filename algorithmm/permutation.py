def permutation(n, lst):
    if n == 5:
        permutations.append(lst[:])
        return

    for i in range(len(arr)):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            permutation(n + 1, lst)
            lst.pop()
            visited[i] = False


arr = [1, 2, 3, 4, 5]
visited = [0] * len(arr)
permutations = []
permutation(0, [])

for perm in permutations:
    print(perm)
