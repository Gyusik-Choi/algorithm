arr = [2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]

max_num = max(arr)
max_arr = [0] * (max_num + 1)
new_arr = [0] * len(arr)
for i in range(len(arr)):
    max_arr[arr[i]] += 1
for i in range(1, len(max_arr)):
    max_arr[i] += max_arr[i - 1]
for i in range(len(new_arr)):
    max_arr[arr[i]] -= 1
    new_arr[max_arr[arr[i]]] = arr[i]
print(new_arr)

# 백준 10989 문제 참고
# 이 문제에서 주의할 점은 메모리 제한이 있기에 배열의 크기를 잡을 때 입력 값의 갯수가 아니라 최대 값을 기준으로 삼아야 한다.
