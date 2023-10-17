def subsets(nums: list[int]):
    n = len(nums)

    def recursion(idx, temp, lst):
        lst.append(temp)

        for i in range(idx, n):
            recursion(i + 1, temp + [nums[i]], lst)

        return lst

    return recursion(0, [], [])


print(subsets([1, 2, 3]))
print(subsets([0]))
