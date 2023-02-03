def teammate(idx):
    global min_difference
    if idx == N // 2:
        if temp_start[0] > N // 4:
            return
        temp_link = []
        for k in range(len(check)):
            if not check[k]:
                temp_link.append(k)
        temp_start_sums = 0
        temp_link_sums = 0
        for l in range(len(temp_start) - 1):
            for m in range(l + 1, len(temp_start)):
                y1 = temp_start[l]
                x1 = temp_start[m]
                y2 = temp_link[l]
                x2 = temp_link[m]
                temp_start_sums += arr[y1][x1] + arr[x1][y1]
                temp_link_sums += arr[y2][x2] + arr[x2][y2]
        min_difference = min(min_difference, abs(temp_start_sums - temp_link_sums))
        return
    else:
        for j in range(N):
            if not temp_start:
                if not check[j]:
                    check[j] = 1
                    temp_start.append(people[j])
                    teammate(idx + 1)
                    check[j] = 0
                    temp_start.pop()
            else:
                last_item = temp_start[-1]
                if not check[j] and people[j] > last_item:
                    check[j] = 1
                    temp_start.append(people[j])
                    teammate(idx + 1)
                    check[j] = 0
                    temp_start.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]
check = [0] * N
temp_start = []
min_difference = float('inf')
teammate(0)
print(min_difference)
