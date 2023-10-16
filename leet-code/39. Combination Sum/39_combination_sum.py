def combination_sum(candidates: list[int], target: int):
    def get_sum(idx, temp: list[int], lst: list[list[int]]):
        temp_sum = sum(temp)

        if temp_sum > target:
            return

        if temp_sum == target:
            lst.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            temp.append(candidates[i])
            get_sum(i, temp, lst)
            temp.pop()

        return lst

    return get_sum(0, [], [])


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
