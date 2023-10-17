def subsets(nums: list[int]):
    n = len(nums)

    def recursion(idx, temp, lst):
        lst.append(temp[:])

        for i in range(idx, n):
            temp.append(nums[i])
            recursion(i + 1, temp, lst)
            temp.pop()

        return lst

    return recursion(0, [], [])


print(subsets([1, 2, 3]))
print(subsets([0]))
