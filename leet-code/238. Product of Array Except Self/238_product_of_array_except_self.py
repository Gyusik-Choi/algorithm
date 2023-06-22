def product_except_self(nums):
    answer = []

    p = 1

    for i in range(len(nums)):
        answer.append(p)
        p *= nums[i]

    p = 1

    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= p
        p *= nums[i]

    return answer


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))

# 1 1 2 6
# 24 12 4 1
# 24 12 8 6
