def customized_merge_sort(arr):
    def is_left_lower(one, two):
        if str(one) + str(two) < str(two) + str(one):
            return True
        return False

    def merge(low, high):
        if low >= high:
            return

        mid = (low + high) // 2
        merge(low, mid)
        merge(mid + 1, high)

        l = low
        m = mid + 1
        temp = []

        while l <= mid and m <= high:
            # 내림차순
            if is_left_lower(arr[l], arr[m]):
                temp.append(arr[m])
                m += 1
            else:
                temp.append(arr[l])
                l += 1

        while m <= high:
            temp.append(arr[m])
            m += 1

        while l <= mid:
            temp.append(arr[l])
            l += 1

        t = 0
        while t < len(temp):
            arr[low + t] = temp[t]
            t += 1

    merge(0, len(arr) - 1)
    return arr


def solution(numbers):
    return str(int(''.join(list(map(lambda x: str(x), customized_merge_sort(numbers))))))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))

# 참고
# https://school.programmers.co.kr/questions/57427
# https://school.programmers.co.kr/questions/51327
