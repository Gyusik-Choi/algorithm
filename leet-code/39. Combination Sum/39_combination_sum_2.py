def combination_sum(candidates: list[int], target: int):
    def get_sum(idx, temp: list[int], lst: list[list[int]]):
        temp_sum = sum(temp)

        if temp_sum > target:
            return

        if temp_sum == target:
            lst.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            # 첫번째 풀이와 달리 재귀 호출 앞 뒤로
            # append, pop 하지 않아도 된다
            get_sum(i, temp + [candidates[i]], lst)

        return lst

    return get_sum(0, [], [])


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
