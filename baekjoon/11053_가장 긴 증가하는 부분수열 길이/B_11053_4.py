def binary_search(start, end, target):
    if start >= end:
        return end

    mid = (start + end) // 2
    if lis[mid] < target:
        start = mid + 1
        return binary_search(start, end, target)
    else:
        if lis[mid] == target:
            return mid
        end = mid
        # end = mid - 1을 하면 안 된다.
        # start 가 0이고 end 가 1이었을때는 mid 가 0이라서 end 를 mid - 1로 하면 인덱스가 맞지 않게 된다.
        return binary_search(start, end, target)


N = int(input())
numbers = list(map(int, input().split()))

lis = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] > lis[-1]:
        lis.append(numbers[i])
    else:
        idx = binary_search(0, len(lis) - 1, numbers[i])
        lis[idx] = numbers[i]

print(len(lis))

# 참고
# https://chanhuiseok.github.io/posts/algo-49/
# https://shoark7.github.io/programming/algorithm/3-LIS-algorithms
