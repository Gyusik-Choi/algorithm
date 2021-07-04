T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers_with_idx = []
    for i in range(N):
        numbers_with_idx.append([numbers[i], i])

    cnt = 1
    while True:
        max_number = numbers_with_idx[0][0]
        flag = False
        if N > 1:
            for j in range(1, len(numbers_with_idx)):
                if max_number < numbers_with_idx[j][0]:
                    max_number = numbers_with_idx[j][0]

            if max_number == numbers_with_idx[0][0] and M == numbers_with_idx[0][1]:
                print(cnt)
                flag = True
                break
            else:
                pop_number_with_idx = numbers_with_idx.pop(0)
                if max_number != pop_number_with_idx[0]:
                    numbers_with_idx.append(pop_number_with_idx)
                elif max_number == pop_number_with_idx[0] and M != pop_number_with_idx[1]:
                    cnt += 1

            if flag:
                break
        else:
            print(1)
            break
