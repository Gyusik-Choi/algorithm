N, K = map(int, input().split())
visited = [0] * N
numbers = []
last_index = 0

while True:
    cnt = K - 1
    idx = last_index
    while cnt > 0:
        idx += 1
        idx %= N
        if not visited[idx]:
            cnt -= 1
    
    if len(numbers) == N - 1:
        numbers.append(idx + 1)
        break
    else:
        visited[idx] = 1
        numbers.append(idx + 1)
        find_idx = N
        while find_idx > 0:
            find_idx -= 1
            idx += 1
            idx %= N
            if not visited[idx]:
                last_index = idx
                break
            

answer = "<"
for number in numbers:
    answer += str(number) + ", "
answer = answer.rstrip(", ")
answer += ">"
print(answer)