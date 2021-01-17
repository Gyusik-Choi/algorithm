N = input()
arr = []
for i in range(len(N)):
    arr.append(int(N[i]))

arr.sort(reverse=True)
arr = map(str, arr)
print(''.join(arr))
