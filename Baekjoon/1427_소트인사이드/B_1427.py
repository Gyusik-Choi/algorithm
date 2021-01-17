N = input()
arr = []
for i in range(len(N)):
    arr.append(int(N[i]))

arr.sort(reverse=True)
for i in range(len(arr)):
    arr[i] = str(arr[i])
print(''.join(arr))
