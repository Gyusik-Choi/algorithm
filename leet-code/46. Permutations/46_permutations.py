def permute(nums: list[int]):
    def get_permutations(temp, perms):
        if len(temp) == len(nums):
            perms.append(temp[:])
            return

        for num in nums:
            if num not in temp:
                temp.append(num)
                get_permutations(temp, perms)
                temp.pop()

        return perms

    return get_permutations([], [])


print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))
