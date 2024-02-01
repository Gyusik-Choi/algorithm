import sys


def find_answer_from_merge_sort(arr, k):
    cnt = 0

    def sort(low, high, answer):
        nonlocal cnt

        if cnt > k:
            return answer

        if low >= high:
            return answer

        mid = (low + high) // 2
        answer = sort(low, mid, answer)
        answer = sort(mid + 1, high, answer)

        l = low
        m = mid + 1
        temp = []

        while l <= mid and m <= high:
            if arr[l] < arr[m]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[m])
                m += 1

        while l <= mid:
            temp.append(arr[l])
            l += 1

        while m <= high:
            temp.append(arr[m])
            m += 1

        for i in range(high - low + 1):
            arr[low + i] = temp[i]

            cnt += 1
            if cnt == k:
                answer = temp[i]
                return answer

        return answer

    return sort(0, len(arr) - 1, -1)


N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
print(find_answer_from_merge_sort(nums, K))
