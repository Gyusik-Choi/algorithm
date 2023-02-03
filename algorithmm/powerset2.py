def subset(nums):
    result = []

    def dfs(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


arr = subset([1, 2, 3])
print(arr)

# 참고
# '파이썬 알고리즘 인터뷰 p.356'